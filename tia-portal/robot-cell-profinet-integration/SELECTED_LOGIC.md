# Selected PLC Logic — Sanitized Portfolio View

The following examples are **sanitized representations** of the reviewed project-specific integration logic. Raw I/O addresses, vendor block implementations and machine-specific identifiers are intentionally omitted.

## Valve-state evaluation

The reviewed valve manager converts open/close feedback into an explicit equipment state:

```scl
IF OpenFeedback AND CloseFeedback THEN
    Valve.State.Faulty := TRUE;

ELSIF OpenFeedback THEN
    Valve.State.Open := TRUE;
    Valve.State.Closed := FALSE;
    Valve.State.Neutral := FALSE;

ELSIF CloseFeedback THEN
    Valve.State.Open := FALSE;
    Valve.State.Closed := TRUE;
    Valve.State.Neutral := FALSE;

ELSE
    Valve.State.Open := FALSE;
    Valve.State.Closed := FALSE;
    Valve.State.Neutral := TRUE;
END_IF;
```

The same pattern is applied across the valve array, giving the rest of the program a consistent equipment-state model.

## Gripper process-data mapping

Raw cyclic communication signals are mapped into structured application data:

```scl
GripperIn.ReadyForOperation := RawIn.ReadyForOperation;
GripperIn.Warning           := RawIn.Warning;
GripperIn.Error             := RawIn.Error;
GripperIn.WorkpieceGripped  := RawIn.WorkpieceGripped;
GripperIn.PositionReached   := RawIn.PositionReached;
GripperIn.ActualPosition    := RawIn.ActualPosition;

RawOut.FastStop       := GripperOut.FastStop;
RawOut.Stop           := GripperOut.Stop;
RawOut.Acknowledge    := GripperOut.Acknowledge;
RawOut.GripWorkpiece  := GripperOut.GripWorkpiece;
RawOut.TargetPosition := GripperOut.TargetPosition;
RawOut.Velocity       := GripperOut.Velocity;
RawOut.GrippingForce  := GripperOut.GrippingForce;
```

This isolates device communication from the higher-level operation logic.

## Parameterized gripper command handling

The application combines a selected operation profile with control commands:

```scl
IF NewCommand THEN
    ActiveParameters := InputOperation;
    ActiveCommand := InputControlCommand;
    NewCommand := FALSE;
END_IF;

IF ActiveCommand.MoveAbsolute THEN
    DeviceCommand.Position := ActiveParameters.Position;
    DeviceCommand.Velocity := ActiveParameters.Velocity;
    DeviceCommand.GrippingForce := ActiveParameters.GrippingForce;
    DeviceCommand.MoveAbsolute := TRUE;
ELSE
    DeviceCommand.MoveAbsolute := FALSE;
END_IF;

IF ActiveCommand.GripAtExpectedPosition THEN
    DeviceCommand.Position := ActiveParameters.Position;
    DeviceCommand.GrippingForce := LIMIT(MinForce, ActiveParameters.GrippingForce, MaxForce);
    DeviceCommand.GripAtExpectedPosition := TRUE;
END_IF;
```

## Robot-triggered valve commands

Robot interface signals are translated into mutually consistent valve commands instead of being connected directly to physical outputs:

```text
Robot requests OPEN    → reset CLOSE/NEUTRAL, set OPEN
Robot requests CLOSE   → reset OPEN/NEUTRAL, set CLOSE
Robot requests NEUTRAL → reset OPEN/CLOSE, set NEUTRAL
```

This pattern is repeated across multiple pneumatic channels.

## System-level fault aggregation

```scl
SystemFault := Device1Fault
            OR Device2Fault
            OR Device3Fault
            OR ...
            OR DeviceNFault;
```

The value is then available to supervisory logic and diagnostics.

## Why these excerpts were selected

These examples show the custom system-integration layer: device abstraction, typed command/status mapping, parameterized operations, robot/equipment coordination and centralized diagnostics. Vendor-owned internal function blocks are intentionally excluded.