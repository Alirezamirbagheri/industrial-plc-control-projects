# Architecture — Pneumatic Flow & Pressure Control

This case study presents the control architecture of the Siemens TIA Portal project without publishing the native engineering archive.

## Functional flow

```text
Digital / analogue sensors
        ↓
Signal and sensor-array mapping
        ↓
Wire-position / process-state evaluation
        ↓
State-machine sequencing
        ↓
Pressure-range / setpoint logic
        ↓
Pressure regulation
        ↓
Pneumatic actuators / valves
        ↓
Status, diagnostics and experiment results
```

## Main control layers

### 1. System sequencing

A top-level PLC state machine coordinates startup, idle, stop/restart and the different experiment/process phases. The implementation separates user/start requests from transition conditions and includes dedicated stuck/recovery and approximation states.

### 2. Sensor abstraction

Twenty discrete sensor channels are mapped into a common Boolean array. This keeps downstream WFE logic independent from raw I/O addresses and makes the tracking/fault-detection blocks operate on a consistent data structure.

### 3. Sensor fault detection

A dedicated SCL block evaluates spatial patterns in the sensor array at a configurable interval. It flags isolated or inconsistent sensor patterns and returns both per-sensor fault flags and an aggregated fault state.

### 4. Wire-position tracking

The WFE position-tracking block uses selected sensors, sensor positions, a target sensor and tolerance window to maintain a compact process state. It detects sensor changes, derives ordered position relative to the target and requires the position to remain within tolerance for a configurable stability time before declaring completion.

### 5. Pressure-control logic

Pressure handling is split between pressure-range / operating-limit logic and state-based pressure regulation. The regulation logic supports a start pressure, pressure increments, maximum pressure, waiting times and a transition into a decreasing/ending phase based on sensor feedback.

## Portfolio scope

The portfolio intentionally excludes native TIA project databases, device packages, network configuration, Siemens library implementations and full HMI exports. The focus is the control decomposition and custom PLC logic.