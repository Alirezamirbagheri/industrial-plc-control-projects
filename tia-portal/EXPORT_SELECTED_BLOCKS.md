# Optional Future TIA Source Export

The initial portfolio version **does not require any additional TIA Portal export**. The reviewed reports were sufficient to prepare the architecture and sanitized logic representations for both Siemens case studies.

If a future version should include exact PLC source/XML rather than sanitized portfolio excerpts, export only blocks that are clearly author-created and redistributable.

## Suitable future candidates

### Pneumatic Flow & Pressure Control

- state-machine logic
- sensor-array mapping
- sensor fault-detection logic
- WFE position tracking
- pressure/setpoint control logic

### Robot Cell & Gripper Integration

- project-specific robot/equipment mapping
- solenoid-valve state handling
- project-specific gripper mapping and operation handling
- system fault aggregation

## Preferred formats

- **External source / SCL** for SCL blocks
- **XML export** for LAD/FBD blocks when available through the engineering workflow

## Never include

- full native `.ap19` / `.zap19` archives
- GSD/GSDML device packages
- passwords, certificates or access-control data
- real IP addresses or identifying device/network names
- logs or generated HMI runtime files
- Siemens, SCHUNK, Zimmer or other vendor-owned library implementations
- restricted course/university material

> Status: **optional future enhancement — no action required for the current portfolio release**.
