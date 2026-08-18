(*
    Portfolio excerpt: cyclic spline point generation
    Derived from the reviewed TwinCAT implementation.
    Not a complete standalone program.

    SegmentWeight represents the normalized per-segment motion allocation
    imported with the offline Python-generated spline data. TotalMotionTime_s
    is selected for the complete mover trajectory and CycleTime_s is the PLC
    point-generation cycle.
*)

(* Allocate cyclic interpolation points for the active segment. *)
SegmentTime_s := TotalMotionTime_s * SegmentWeight / TotalWeight;
NumCyclePoints := LREAL_TO_UDINT(SegmentTime_s / CycleTime_s);
IF NumCyclePoints < 1 THEN
    NumCyclePoints := 1;
END_IF;

(* Advance the normalized spline parameter within the segment. *)
u := uStart
     + (uEnd - uStart)
     * TO_LREAL(PointIndexInSegment)
     / TO_LREAL(NumCyclePoints);

(* Cubic parametric spline evaluation. *)
NextPoint.x := Ax
             + Bx * u
             + Cx * u * u
             + Dx * u * u * u;

NextPoint.y := Ay
             + By * u
             + Cy * u * u
             + Dy * u * u * u;

(* Advance to the next segment after the final cyclic point. *)
IF PointIndexInSegment >= NumCyclePoints THEN
    PointIndexInSegment := 0;
    SegmentIndex := SegmentIndex + 1;
ELSE
    PointIndexInSegment := PointIndexInSegment + 1;
END_IF;
