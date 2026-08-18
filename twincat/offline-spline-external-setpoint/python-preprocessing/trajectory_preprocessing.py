"""Offline trajectory smoothing and parametric-spline export.

Portfolio-safe refactoring of the Python preprocessing used before TwinCAT
execution. The input CSV contains paired X/Y columns for each mover. The
pipeline reduces noisy/redundant simulation points, fits a deviation-bounded
cubic parametric spline, and exports per-segment polynomial/timing parameters
for cyclic PLC evaluation.

No machine-specific paths, TwinCAT configuration, or raw project data are
embedded in this module.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.interpolate import PPoly, interp1d, splev, splprep
from sklearn.neighbors import NearestNeighbors


@dataclass
class SmoothingConfig:
    rdp_tolerance: float = 5.0
    smoothing_factor: float = 5000.0
    max_deviation: float = 10.0
    resample_points: int = 500
    max_points: int = 2000
    spline_order: int = 3


@dataclass
class MoverResult:
    raw_x: np.ndarray
    raw_y: np.ndarray
    clean_x: np.ndarray
    clean_y: np.ndarray
    smooth_x: np.ndarray
    smooth_y: np.ndarray
    tck: tuple | None
    path_length: float
    original_length: float
    max_deviation: float
    mean_deviation: float


def rdp(points: np.ndarray, epsilon: float) -> np.ndarray:
    """Ramer-Douglas-Peucker polyline simplification."""
    if len(points) < 3:
        return points.copy()

    start, end = points[0], points[-1]
    segment = end - start
    segment_len_sq = float(segment.dot(segment))

    if segment_len_sq == 0.0:
        distances = np.linalg.norm(points - start, axis=1)
    else:
        t = np.clip(((points - start).dot(segment)) / segment_len_sq, 0.0, 1.0)
        projection = start + np.outer(t, segment)
        distances = np.linalg.norm(points - projection, axis=1)

    split_index = int(np.argmax(distances))
    if distances[split_index] > epsilon:
        left = rdp(points[: split_index + 1], epsilon)
        right = rdp(points[split_index:], epsilon)
        return np.vstack((left[:-1], right))

    return np.vstack((start, end))


def remove_duplicate_points(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Remove repeated coordinates while preserving first-occurrence order."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    coordinates = np.column_stack((x, y))
    _, unique_indices = np.unique(np.round(coordinates, 6), axis=0, return_index=True)
    unique_indices = np.sort(unique_indices)

    x_unique = x[unique_indices]
    y_unique = y[unique_indices]
    if len(x_unique) < 3:
        raise ValueError("At least three unique trajectory points are required.")
    return x_unique, y_unique


def arc_length_parameter(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Normalized cumulative arc-length parameter in [0, 1]."""
    distances = np.hypot(np.diff(x), np.diff(y))
    cumulative = np.insert(np.cumsum(distances), 0, 0.0)
    return cumulative / cumulative[-1] if cumulative[-1] > 0 else cumulative


def path_length(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.sum(np.hypot(np.diff(x), np.diff(y))))


def deviation_to_smoothed(
    original_x: np.ndarray,
    original_y: np.ndarray,
    smoothed_x: np.ndarray,
    smoothed_y: np.ndarray,
) -> tuple[float, float]:
    """Maximum and mean point-to-smoothed-trajectory nearest distance."""
    original = np.column_stack((original_x, original_y))
    smoothed = np.column_stack((smoothed_x, smoothed_y))
    nearest = NearestNeighbors(n_neighbors=1).fit(smoothed)
    distances, _ = nearest.kneighbors(original)
    return float(np.max(distances)), float(np.mean(distances))


def smooth_mover(x_raw: np.ndarray, y_raw: np.ndarray, cfg: SmoothingConfig) -> MoverResult:
    try:
        x_clean, y_clean = remove_duplicate_points(x_raw, y_raw)
    except ValueError:
        x_clean = np.asarray(x_raw, dtype=float)
        y_clean = np.asarray(y_raw, dtype=float)

    simplified = rdp(np.column_stack((x_clean, y_clean)), cfg.rdp_tolerance)
    if len(simplified) < 3:
        simplified = np.column_stack((x_clean, y_clean))

    x_simple, y_simple = simplified[:, 0], simplified[:, 1]
    u_simple = arc_length_parameter(x_simple, y_simple)

    n_resample = max(min(cfg.resample_points, cfg.max_points), len(x_simple))
    u_uniform = np.linspace(0.0, 1.0, n_resample)
    x_resampled = interp1d(u_simple, x_simple, kind="linear", fill_value="extrapolate")(u_uniform)
    y_resampled = interp1d(u_simple, y_simple, kind="linear", fill_value="extrapolate")(u_uniform)

    spline_order = min(cfg.spline_order, len(x_resampled) - 1)
    smoothing = cfg.smoothing_factor
    tck = None

    while True:
        try:
            tck, _ = splprep(
                [x_resampled, y_resampled],
                u=u_uniform,
                s=smoothing,
                k=spline_order,
            )
            x_smooth, y_smooth = splev(u_uniform, tck)
            x_smooth = np.asarray(x_smooth)
            y_smooth = np.asarray(y_smooth)

            # Preserve exact trajectory endpoints for handover to the PLC path.
            x_smooth[0], y_smooth[0] = x_clean[0], y_clean[0]
            x_smooth[-1], y_smooth[-1] = x_clean[-1], y_clean[-1]

            max_dev, mean_dev = deviation_to_smoothed(
                x_clean, y_clean, x_smooth, y_smooth
            )
            if max_dev <= cfg.max_deviation or smoothing < 1e-3:
                break
            smoothing *= 0.5
        except Exception:
            tck = None
            x_smooth, y_smooth = x_resampled, y_resampled
            max_dev, mean_dev = deviation_to_smoothed(
                x_clean, y_clean, x_smooth, y_smooth
            )
            break

    return MoverResult(
        raw_x=np.asarray(x_raw, dtype=float),
        raw_y=np.asarray(y_raw, dtype=float),
        clean_x=x_clean,
        clean_y=y_clean,
        smooth_x=np.asarray(x_smooth),
        smooth_y=np.asarray(y_smooth),
        tck=tck,
        path_length=path_length(x_smooth, y_smooth),
        original_length=path_length(x_clean, y_clean),
        max_deviation=max_dev,
        mean_deviation=mean_dev,
    )


def local_to_global_cubic(coefficients: np.ndarray, u0: float) -> tuple[float, float, float, float]:
    """Convert PPoly local cubic coefficients to A + B*u + C*u^2 + D*u^3."""
    a3, a2, a1, a0 = coefficients
    d = a3
    c = a2 - 3.0 * a3 * u0
    b = a1 - 2.0 * a2 * u0 + 3.0 * a3 * u0**2
    a = a0 - a1 * u0 + a2 * u0**2 - a3 * u0**3
    return float(a), float(b), float(c), float(d)


def segment_rows(mover_id: int, result: MoverResult) -> list[dict[str, float | int]]:
    """Build one CSV row per non-zero-length spline segment."""
    if result.tck is None:
        return []

    knots, coefficients, order = result.tck
    # Work on copies so the stored fit is not modified by export preparation.
    x_coeff = np.asarray(coefficients[0], dtype=float).copy()
    y_coeff = np.asarray(coefficients[1], dtype=float).copy()
    x_coeff[0], y_coeff[0] = result.smooth_x[0], result.smooth_y[0]
    x_coeff[-1], y_coeff[-1] = result.smooth_x[-1], result.smooth_y[-1]

    ppx = PPoly.from_spline((knots, x_coeff, order))
    ppy = PPoly.from_spline((knots, y_coeff, order))
    valid = [
        index
        for index in range(len(ppx.x) - 1)
        if abs(ppx.x[index + 1] - ppx.x[index]) > 1e-9
    ]

    raw_u = arc_length_parameter(result.raw_x, result.raw_y)
    smooth_u = arc_length_parameter(result.smooth_x, result.smooth_y)
    # Preserve the project's temporal mapping: each raw simulation point is
    # associated with the closest normalized-progress sample on the smoothed path.
    raw_to_smooth_index = np.argmin(
        np.abs(raw_u[:, None] - smooth_u[None, :]), axis=1
    )
    raw_dist_to_previous = np.hypot(
        np.diff(result.raw_x, prepend=result.raw_x[0]),
        np.diff(result.raw_y, prepend=result.raw_y[0]),
    )

    rows: list[dict[str, float | int]] = []
    for segment_number, index in enumerate(valid, start=1):
        u_start = float(ppx.x[index])
        u_end = float(ppx.x[index + 1])
        ax, bx, cx, dx = local_to_global_cubic(ppx.c[:, index], u_start)
        ay, by, cy, dy = local_to_global_cubic(ppy.c[:, index], u_start)

        u_eval = np.linspace(u_start, u_end, 200)
        x_eval = ax + bx * u_eval + cx * u_eval**2 + dx * u_eval**3
        y_eval = ay + by * u_eval + cy * u_eval**2 + dy * u_eval**3
        length_mm = path_length(x_eval, y_eval)

        # Raw samples are the temporal trace from the simulation. Map them to
        # the smoothed samples belonging to this spline segment, as in the
        # original project pipeline.
        smooth_indices = np.where((smooth_u >= u_start) & (smooth_u <= u_end))[0]
        in_segment = np.isin(raw_to_smooth_index, smooth_indices)

        num_raw = int(np.count_nonzero(in_segment))
        raw_distance = float(np.sum(raw_dist_to_previous[in_segment]))

        rows.append(
            {
                "Mover": mover_id,
                "Segment": segment_number,
                "U_Start": u_start,
                "U_End": u_end,
                "Ax": ax,
                "Bx": bx,
                "Cx": cx,
                "Dx": dx,
                "Ay": ay,
                "By": by,
                "Cy": cy,
                "Dy": dy,
                "Length_mm": length_mm,
                "Length_Weight": length_mm / result.path_length if result.path_length > 1e-9 else 0.0,
                "NumRawPoints": num_raw,
                "RawDistanceSum": raw_distance,
            }
        )

    total_raw = sum(int(row["NumRawPoints"]) for row in rows)
    for row in rows:
        row["RawPointsWeight"] = (
            float(row["NumRawPoints"]) / total_raw if total_raw > 0 else 0.0
        )
        raw_distance = max(float(row["RawDistanceSum"]), 1e-9)
        row["Time_Scale_Factor"] = (
            float(row["Length_mm"]) / raw_distance
        ) * float(row["RawPointsWeight"])

    time_sum = sum(float(row["Time_Scale_Factor"]) for row in rows)
    if time_sum > 0:
        for row in rows:
            row["Time_Scale_Factor"] = float(row["Time_Scale_Factor"]) / time_sum

    return rows


def process_csv(input_csv: Path, output_csv: Path, cfg: SmoothingConfig) -> list[MoverResult]:
    data = pd.read_csv(input_csv)
    if data.shape[1] < 2 or data.shape[1] % 2 != 0:
        raise ValueError("Input CSV must contain paired X/Y columns for each mover.")

    results: list[MoverResult] = []
    all_rows: list[dict[str, float | int]] = []

    for mover_index in range(data.shape[1] // 2):
        x_raw = data.iloc[:, mover_index * 2].astype(float).to_numpy()
        y_raw = data.iloc[:, mover_index * 2 + 1].astype(float).to_numpy()
        result = smooth_mover(x_raw, y_raw, cfg)
        results.append(result)
        all_rows.extend(segment_rows(mover_index + 1, result))
        print(
            f"Mover {mover_index + 1}: raw={len(x_raw)}, "
            f"smoothed={len(result.smooth_x)}, "
            f"length={result.path_length:.2f}, "
            f"max_dev={result.max_deviation:.2f}"
        )

    fieldnames = [
        "Mover",
        "Segment",
        "U_Start",
        "U_End",
        "Ax",
        "Bx",
        "Cx",
        "Dx",
        "Ay",
        "By",
        "Cy",
        "Dy",
        "Length_mm",
        "Length_Weight",
        "Time_Scale_Factor",
        "NumRawPoints",
        "RawPointsWeight",
        "RawDistanceSum",
    ]
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reduce, smooth and convert multi-mover trajectories to parametric spline segments."
    )
    parser.add_argument("input_csv", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("ParametricSplineCoeff.csv"),
        help="Output spline-parameter CSV.",
    )
    parser.add_argument("--rdp", type=float, default=5.0, help="RDP tolerance.")
    parser.add_argument("--smooth", type=float, default=5000.0, help="Initial spline smoothing factor.")
    parser.add_argument("--max-deviation", type=float, default=10.0, help="Maximum allowed geometric deviation.")
    parser.add_argument("--samples", type=int, default=500, help="Resampled points per mover.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = SmoothingConfig(
        rdp_tolerance=args.rdp,
        smoothing_factor=args.smooth,
        max_deviation=args.max_deviation,
        resample_points=args.samples,
    )
    process_csv(args.input_csv, args.output, cfg)
    print(f"Spline parameter CSV written to: {args.output}")


if __name__ == "__main__":
    main()
