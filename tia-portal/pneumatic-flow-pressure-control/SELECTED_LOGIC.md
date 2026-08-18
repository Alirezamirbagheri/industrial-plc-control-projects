# Selected PLC Logic — Sanitized Portfolio View

The following excerpts are **sanitized representations** of the reviewed project logic. Hardware addresses, project-specific identifiers and vendor code are intentionally omitted.

## Sensor-array mapping

A dedicated mapping layer converts physical sensor channels into a common array used by the WFE logic:

```scl
FOR i := 1 TO NumSensors DO
    Sensors[i] := DigitalSensor[i];
END_FOR;
```

This abstraction lets tracking, fault detection and process-state logic operate independently from raw PLC I/O addressing.

## Pattern-based sensor fault detection

The reviewed project contains periodic checks for spatially inconsistent sensor patterns. Conceptually:

```scl
IF CheckTimer.Q THEN
    FOR i := 3 TO NumOperatingSensors - 3 DO
        IF Sensors[i-2] AND Sensors[i-1]
           AND NOT Sensors[i]
           AND Sensors[i+1] AND Sensors[i+2] THEN
            FaultySensor[i] := TRUE;
            FaultyState := TRUE;
        END_IF;

        (* Additional multi-sensor consistency rules are evaluated here. *)
    END_FOR;
END_IF;
```

The original implementation evaluates several local patterns and produces both an array of faulty sensors and an overall fault state.

## Position tracking with tolerance and stability time

The WFE tracker maintains an internal state machine and detects transitions in selected sensors:

```scl
CASE State OF
    Started:
        LastSensorState := Sensors;
        State := Stabilizing;

    Stabilizing:
        FOR i := 1 TO NumSensors DO
            IF SelectedSensors[i] AND (Sensors[i] <> LastSensorState[i]) THEN
                LastSensorPosition := i;
                LastSensorState[i] := Sensors[i];
            END_IF;
        END_FOR;

        SignedDistance := LastSensorOrderPosition - TargetSensorOrder;

        IF ABS(SignedDistance) <= Tolerance THEN
            StabilityTimer(IN := TRUE, PT := StabilityTime);
            IF StabilityTimer.Q THEN
                State := Finished;
            END_IF;
        ELSE
            StabilityTimer(IN := FALSE, PT := StabilityTime);
        END_IF;
END_CASE;
```

## State-based pressure increase

The pressure-control concept increases pressure in timed steps and reacts to sensor feedback or a configured maximum:

```scl
CASE OperationState OF
    Ready:
        IF StartCondition THEN
            CurrentPressure := StartPressure;
            OperationState := Running;
        END_IF;

    Running:
        StepTimer(IN := TRUE, PT := PressureStepTime);

        IF StepTimer.Q AND NOT MaxPressureReached THEN
            CurrentPressure := CurrentPressure + PressureStep;
            StepTimer(IN := FALSE, PT := PressureStepTime);
        END_IF;

        IF CurrentPressure >= MaxPressure THEN
            MaxPressureReached := TRUE;
        END_IF;

        IF PresenceSensor THEN
            OperationState := Decelerating;
        END_IF;
END_CASE;
```

## Why these excerpts were selected

They demonstrate four reusable engineering ideas from the project: I/O abstraction, rule-based diagnostics, sensor-driven state estimation and deterministic PLC-side process control. Full native blocks and vendor libraries are intentionally not reproduced.