# Industrial PLC Control Projects

Portfolio repository for selected industrial-automation work using **Siemens TIA Portal** and **Beckhoff TwinCAT 3**.

The repository is organized as four separate case studies: two Siemens PLC projects and two Beckhoff TwinCAT projects. Public material is limited to engineering content that can be redistributed safely; native vendor projects, proprietary libraries, license material, machine-specific configuration and restricted assets remain excluded.

## Portfolio structure

### Siemens TIA Portal — Case Study 1

Sanitized presentation of the first Siemens PLC project, focusing on the control logic, sequencing, I/O architecture, communication and diagnostics authored for the project.

### Siemens TIA Portal — Case Study 2

Sanitized presentation of the second Siemens PLC project, kept separate because it represents a distinct automation implementation and engineering task.

See [`tia-portal/README.md`](tia-portal/README.md).

### Beckhoff TwinCAT — Offline Spline External Setpoint Generation

Offline trajectory-execution project in which spline parameters are prepared externally and imported into TwinCAT. The PLC evaluates the trajectory cyclically and generates motion setpoints through an external-setpoint-generation concept, allowing the mover to follow the reconstructed spline path point by point.

See [`twincat/offline-spline-external-setpoint/README.md`](twincat/offline-spline-external-setpoint/README.md).

### Beckhoff TwinCAT — Online Python/Vision Motion Planning

Online closed-loop project coupling TwinCAT with Python-based perception and motion planning. Camera data is processed in Python, motion/path decisions are generated online, and TwinCAT handles synchronized execution and PLC-side runtime control.

See [`twincat/online-python-vision-motion-planning/README.md`](twincat/online-python-vision-motion-planning/README.md).

## Engineering themes

- PLC sequencing and state-machine logic
- IEC 61131-3 / Structured Text, SCL, LAD and FBD concepts
- Profinet and ADS communication
- cyclic setpoint generation and motion execution
- XPlanar / multi-mover control concepts
- Python–PLC integration
- computer-vision-assisted automation
- fault handling, synchronization and diagnostics

## Public-release approach

The **native engineering projects are not published by default**. Before anything is made public, the content is reviewed to exclude:

- vendor-owned or third-party libraries and binaries
- license files, certificates and activation material
- passwords, tokens or credentials
- real IP addresses, AMS Net IDs and machine/network identifiers
- confidential customer, employer or university material
- datasets, logs or screenshots containing restricted information
- generated or compiled artifacts that are not needed to demonstrate the engineering work

The public version should contain only material that can be redistributed safely and that clearly demonstrates the engineering contribution.

## Repository layout

```text
tia-portal/
  README.md
  project-1/                         planned sanitized case study
  project-2/                         planned sanitized case study

twincat/
  README.md
  offline-spline-external-setpoint/  offline spline / cyclic setpoint project
  online-python-vision-motion-planning/ online Python + vision + planning project

PUBLIC_RELEASE_CHECKLIST.md
```

## License

No open-source license is assigned yet. A license will only be selected after the included source files and third-party dependencies have been reviewed for redistribution rights.
