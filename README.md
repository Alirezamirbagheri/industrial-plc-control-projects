# Industrial PLC Control Projects

Portfolio repository for industrial automation work using **Siemens TIA Portal** and **Beckhoff TwinCAT**.

The goal of this repository is to present selected PLC logic, sequencing, communication and motion-control concepts in a clean, vendor-safe format without publishing proprietary libraries, license material, machine-specific configuration or restricted project assets.

## Projects

### Siemens TIA Portal

Planned public material will focus on engineering content authored for the project, such as:

- PLC sequencing and state-machine logic
- SCL/LAD/FBD logic where redistribution is permitted
- I/O and control architecture
- Profinet / device communication concepts
- HMI or diagnostic concepts using sanitized screenshots or diagrams
- Short explanation of the engineering problem and implemented solution

See [`tia-portal/README.md`](tia-portal/README.md).

### Beckhoff TwinCAT

Planned public material will focus on reusable automation concepts, such as:

- IEC 61131-3 / Structured Text logic authored for the project
- State-machine and synchronization logic
- ADS communication concepts
- Motion / mover control concepts where applicable
- Sanitized architecture diagrams and selected code excerpts

See [`twincat/README.md`](twincat/README.md).

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
tia-portal/                 Siemens PLC project documentation / sanitized exports
twincat/                    Beckhoff PLC project documentation / sanitized exports
PUBLIC_RELEASE_CHECKLIST.md publication-safety checklist
```

## License

No open-source license is assigned yet. A license will only be selected after the included source files and third-party dependencies have been reviewed for redistribution rights.
