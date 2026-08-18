# Siemens TIA Portal Case Studies

The reviewed Siemens material contains two distinct automation projects and is therefore presented as two separate case studies inside this repository.

## 1. Pneumatic Flow & Pressure Control

A PLC/HMI project centered on pneumatic process control and measurement. The reviewed project shows:

- ET 200SP distributed I/O
- Siemens CM 4xIO-Link integration
- Festo VPPM proportional-pressure devices
- pressure and flow signals
- PID_Compact-based regulation
- WinCC Runtime Advanced / HMI engineering
- alarm, logging and diagnostic concepts

See [`pneumatic-flow-pressure-control/README.md`](pneumatic-flow-pressure-control/README.md).

## 2. Robot Cell & Gripper Integration

A larger multi-device automation project. The reviewed project shows:

- Siemens S7-1500-class control, including a CPU 1517TF-3 PN/DP project configuration
- ET 200SP distributed I/O
- FANUC robot interfaces
- SCHUNK EGK-series gripper integration
- Festo CPX / pneumatic valve hardware
- PROFINET and PROFIsafe device communication
- Siemens TP1500 Comfort PRO HMI
- operation selection, handshakes, safety/status handling and diagnostics

See [`robot-cell-profinet-integration/README.md`](robot-cell-profinet-integration/README.md).

## Publication scope

The original TIA Portal archives are not suitable for direct publication. They contain vendor GSD/GSDML material, internal project databases, generated HMI runtime artifacts, logs and machine/network configuration. Public content should therefore be limited to sanitized engineering documentation, selected author-created PLC logic/exports, and safe diagrams or screenshots.

> Status: **source archives reviewed; public extraction still intentionally conservative**.
