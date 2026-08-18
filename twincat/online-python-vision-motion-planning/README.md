# Online Python/Vision Motion Planning with TwinCAT

TwinCAT 3 case study for online, closed-loop motion execution coupled with Python-based computer vision and motion planning.

## Control concept

Camera data is processed on the Python side to estimate the current system state and support online planning. Python and TwinCAT exchange runtime data and commands so that newly generated motion decisions can be executed by the PLC while preserving synchronization, state-machine supervision and deterministic machine-side control.

## Engineering focus

- Python–TwinCAT communication
- camera-driven state/perception updates
- online path / motion generation
- synchronized multi-mover execution
- command and acknowledgement handshakes
- PLC runtime state machine
- local motion overrides / online corrections where required
- fault handling and execution supervision

## System role

This PLC project forms the machine-execution side of the larger AI-based wire-harness system, connecting online perception and planning with industrial motion control.

## Portfolio release

The public version will contain only sanitized, author-created engineering logic and documentation. Native TwinCAT workspaces, vendor libraries, compiled artifacts, licenses, certificates, real AMS Net IDs/IP addresses and machine-specific configuration are excluded by default.

> Status: **private staging area — source extraction and review pending**.
