# Industrial PLC Control Projects

Portfolio repository for selected industrial-automation work using **Siemens TIA Portal** and **Beckhoff TwinCAT 3**.

The source archives have been reviewed and are represented here as **four separate engineering case studies**: two Siemens PLC projects and two Beckhoff TwinCAT projects. Native vendor projects, proprietary libraries, license material, machine-specific configuration, raw logs and restricted assets remain excluded.

## Case studies

### 1. Siemens TIA Portal — Pneumatic Flow & Pressure Control

PLC/HMI project for pneumatic process control using distributed I/O, IO-Link devices and PID-based regulation. The reviewed project includes ET 200SP I/O, a Siemens IO-Link master, Festo proportional-pressure hardware, PID_Compact logic and WinCC HMI functionality.

**Portfolio focus:** PID control, pressure/flow handling, IO-Link integration, distributed I/O, alarms/diagnostics and HMI engineering.

See [`tia-portal/pneumatic-flow-pressure-control/README.md`](tia-portal/pneumatic-flow-pressure-control/README.md).

### 2. Siemens TIA Portal — Robot Cell & Gripper Integration

Multi-device automation project integrating Siemens PLC control with robot, gripper, pneumatic and HMI subsystems over industrial Ethernet. The reviewed project contains FANUC robot interfaces, a SCHUNK gripper, Festo pneumatic/valve hardware, ET 200SP, PROFINET/PROFIsafe and a Siemens comfort-panel HMI.

**Portfolio focus:** multi-device integration, robot handshakes, gripper control, distributed I/O, PROFINET/PROFIsafe, sequencing and HMI diagnostics.

See [`tia-portal/robot-cell-profinet-integration/README.md`](tia-portal/robot-cell-profinet-integration/README.md).

### 3. Beckhoff TwinCAT — Offline Spline External Setpoint Generation

Offline trajectory-execution project in which parametric spline coefficients are generated externally and imported into TwinCAT. The PLC evaluates the spline cyclically, reconstructs the next trajectory point and drives XPlanar movers through an external-setpoint-generation concept.

**Portfolio focus:** spline import/evaluation, cyclic point generation, timing allocation, mover execution and deterministic motion logic.

This case study now includes a sanitized architecture document and a Structured Text source excerpt.

See [`twincat/offline-spline-external-setpoint/README.md`](twincat/offline-spline-external-setpoint/README.md).

### 4. Beckhoff TwinCAT — Online Python/Vision Motion Planning

Closed-loop automation project coupling TwinCAT with Python-based perception and online motion planning. Python produces global motion plans and local overrides from camera/perception data; TwinCAT manages command/acknowledgement handshakes, synchronized execution, mover state and PLC-side runtime supervision.

**Portfolio focus:** Python–PLC coupling, online global plans, local override priority, state-machine coordination, synchronized multi-mover execution and motion tracing.

This case study now includes a sanitized architecture document and Structured Text excerpts for the global-plan handshake and local-override priority logic.

See [`twincat/online-python-vision-motion-planning/README.md`](twincat/online-python-vision-motion-planning/README.md).

## Engineering themes

- IEC 61131-3 PLC programming and state-machine design
- Siemens TIA Portal / WinCC and Beckhoff TwinCAT 3
- PROFINET, PROFIsafe, IO-Link and ADS communication concepts
- PID-based pneumatic control
- robot and gripper integration
- cyclic setpoint generation and XPlanar motion execution
- Python–PLC integration and online planning
- fault handling, synchronization, diagnostics and HMI design

## Current publication status

- **TwinCAT offline:** reviewed and sanitized architecture/source excerpt prepared
- **TwinCAT online:** reviewed and sanitized architecture/source excerpts prepared
- **TIA pneumatic control:** documentation prepared; selected PLC block export still required
- **TIA robot cell:** documentation prepared; selected PLC block export still required

The native engineering archives are **not** published. The review identified vendor packages, compiled libraries, license files, project databases, target-system/network configuration, raw logs and other generated artifacts that should remain outside a public portfolio.

## Repository layout

```text
tia-portal/
  README.md
  EXPORT_SELECTED_BLOCKS.md
  pneumatic-flow-pressure-control/
  robot-cell-profinet-integration/

twincat/
  offline-spline-external-setpoint/
    ARCHITECTURE.md
    source-excerpts/
  online-python-vision-motion-planning/
    ARCHITECTURE.md
    source-excerpts/

PUBLIC_RELEASE_CHECKLIST.md
REVIEW_STATUS.md
```

## License

No open-source license is assigned yet. A license will only be selected after the exact source files intended for public release have been reviewed for ownership and redistribution rights.
