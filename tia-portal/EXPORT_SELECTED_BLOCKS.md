# Export Selected PLC Blocks from TIA Portal

The native TIA Portal archives should remain private. For the public portfolio, export only selected PLC blocks that you authored and that do not contain restricted customer, university, vendor or machine-specific information.

## Pneumatic Flow & Pressure Control

Export the blocks that best demonstrate:

- pressure / flow scaling and signal handling
- IO-Link process-data mapping
- PID control or setpoint handling
- operating sequence / state logic
- HMI command and diagnostic interface

Preferred formats: **External source / SCL** for SCL blocks, or **XML export** for LAD/FBD blocks.

## Robot Cell & Gripper Integration

Export the blocks that best demonstrate:

- robot command/status handshake
- gripper command/status logic
- operating sequence / state machine
- device-ready / fault interlocks
- HMI command/status interface

Preferred formats: **External source / SCL** for SCL blocks, or **XML export** for LAD/FBD blocks.

## Before exporting

Do not include:

- full native `.ap19` / `.zap19` project archives
- GSD/GSDML device packages
- passwords, certificates or access-control data
- real IP addresses / device names if they identify the actual lab network
- logs or generated HMI runtime files
- blocks copied from vendor libraries or course templates unless redistribution is clearly permitted

After the exports are added to the private staging repository, they can be reviewed and sanitized before the repository is made public.
