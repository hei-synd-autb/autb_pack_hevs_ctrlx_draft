# More info
[Advanced automation](https://github.com/hei-synd-aaut/aaut-docs)

See modules 06/07/08

# Most advanced lab, reference.

## [Lab 06 Autb](https://github.com/hei-synd-autb/autb-lab-06_2025)

Note: use Version 2.6 : CtrlX_2025_AutB_06_v_2_6.projectarchive

### To start the project:
Extract the archive.
Start node-red flow by:

1.  launch command prompt.
1.  change directory to the directory of the projet, for example ``cd: C:\Users\cedric.lenoir\Documents\Git\autb-lab-06_2025\PracticalWork_06_Student``
1.  node-red

### What you can do
From the UI, you can clear, init the axes.
In Exectute and Manual, you can jog the axes and open/close the gripper.

### Error from version 2.6
With the new version, some internal alarms of the core are cannot be reset from PLC, you have to reset them in : ``https://192.168.0.200/device-dashboard`` otherwise the state machine can be blocked in a state.

