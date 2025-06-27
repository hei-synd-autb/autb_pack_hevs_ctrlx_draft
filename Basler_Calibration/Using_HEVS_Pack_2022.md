<h1 align="left">
  <br>
  <img src="./img/hei-en.png" alt="HEI-Vs Logo" width="350">
  <br>
  HEI-Vs Engineering School
  <br>
</h1>

# Using HEVS_Pack_2022

This is a short explanation of the use of Pack in This programm.

2022 refer to the last reference [ISA-TR88.00.02-**2022**, Machine and Unit States: An implementation example of ISA-88.00.01](https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp)

The HEVS pack run on a programm:

## Preliminary documentation
The documentation is started during implementation but not complete.

On GitLAB [HEVS_CtrlX_Pack](https://gitlab.hevs.ch/infrastructure/labos/automation-box/technicalreviews/hevs_ctrlx_pack/-/tree/main?ref_type=heads)

There is a version for Beckhoff too [HEVS_TwinCAT_Pack](https://gitlab.hevs.ch/infrastructure/labos/automation-box/technicalreviews/hevs_twincat_pack).


## PLC_PACK

```iecst
PROGRAM PLC_PACK
VAR
	uliCount: ULINT;
    	
```

### SC State Complete
```iecst
(*
	Manage states and mode.
    Receive a AND of SC of each module
*)
whatSC := fbModuleTest.SC 	AND
          fbModuleOne.SC  	AND
		  fbModuleTwo.SC  	AND
		  fbModuleThree.SC	AND
		// Try to integrate 3 FB_ModuleAxis from another program
		// But other Task
		  PRG_Process.fbModuleAxis_X.SC AND
		  PRG_Process.fbModuleAxis_Y.SC AND
		  PRG_Process.fbModuleAxis_Z.SC AND
          PRG_PackModule_Template.SC;
```

In the example above, different modules are integrated.

You can see in ``HEVS_Robot``, ``FB_ModuleAxis`` how the Pack is used for a Control Module.

### FB_ModuleAxis

#### Example: Clearing

```iecst
(*
	Manage Clearing
*)

// actualState is actual state of Unit from:
//	PackTag.Status.StateCurrent
//
// Wait for : stActing.Clearing_SC : TRUE
// While not all units SC, actualState remains in eClearing.
//
// From PLCopen Motion, the axis at start could be
// Standstill	--> Enabled
// Disabled		--> Need an enable for SC
// ErrorStop	--> Need a reset befoire to be enabled
IF actualState = E_PackState.eClearing THEN
	CASE axisClearing OF
		E_AxisClearing.eIdle :
			IF mcReadStatus.Standstill THEN
				axisClearing := E_AxisClearing.eEnabled;
			ELSIF mcReadStatus.ErrorStop THEN
				axisClearing := E_AxisClearing.eErrorStop;
			ELSE
				axisClearing := E_AxisClearing.eDisabled;
			END_IF
		
		E_AxisClearing.eErrorStop :
			IF mcReadStatus.Standstill THEN
				axisClearing := E_AxisClearing.eEnabled;
			ELSE
				axisClearing := E_AxisClearing.eDisabled;
			END_IF
		
		E_AxisClearing.eDisabled  :
			IF mcReadStatus.Standstill THEN
				axisClearing := E_AxisClearing.eEnabled;
			ELSIF mcReadStatus.ErrorStop THEN
				axisClearing := E_AxisClearing.eErrorStop;
			END_IF
		
		E_AxisClearing.eEnabled   :
			IF mcReadStatus.ErrorStop THEN
				axisClearing := E_AxisClearing.eErrorStop;
			END_IF
	END_CASE
	stActing.Clearing_SC := (axisClearing = E_AxisClearing.eEnabled);
ELSE
	stActing.Clearing_SC := FALSE;
	axisClearing := E_AxisClearing.eIdle; 
END_IF

```

> Note :
>   > ``stActing.Clearing_SC := FALSE;``        // to be reset when end of clearing
>   > ``axisClearing := E_AxisClearing.eIdle;`` // Set the state machine for next entry in clearing. Could be something else, for example when Suspended.

---

# PRG_PackModule_Template

## Header

```iecst
PROGRAM PRG_PackModule_Template
VAR_IN_OUT
	Status_StateCurrent: DINT;			// has to take the PackTag Status.StateCurrent
END_VAR
VAR
	uliLoop                     : ULINT;
	/// Store last cycle at the en of FB call to detect and state change
	/// Used to force minimum of one testSC.In = 0 and reset SC once between each SC
	stateLastCycie: E_PackState := E_PackState.eUndefined;
	actualState: E_PackState    := E_PackState.eAborted;
	init                        : BOOL;
	testSC                      : TON;
	// This Flag is used as result on SC State complete.
	setSC                       : BOOL;
	stActing                    : ST_Acting;
	// For test, wait variable TRUE for resetting SC
	LockResetting               : BOOL;
END_VAR

```

## Core of the program

```iecst
uliLoop := uliLoop + 1;
IF NOT init THEN
    init := TRUE;
END_IF
actualState := Status_StateCurrent;

(*
	Your code here
	For code in States, modify the actions. ACT
	
	Code for mode is still not impletemented
*)

ACT_Aborting();
ACT_Clearing();
ACT_Completing();
ACT_Execute();
ACT_Holding();
ACT_Resetting();
ACT_Starting();
ACT_Stopping();
ACT_Suspending();
ACT_Unholding();
ACT_Unsuspending();

(*
	Footer, do not modify the code below.

	For test of State Machine, we use a timer.
	Its allow to have some time to visualise it
	We could remove this timer in production version
*)
testSC(IN := stActing.Clearing_SC       OR
             stActing.Starting_SC      	OR
             stActing.Execute_SC       	OR
             stActing.Stopping_SC      	OR
             stActing.Aborting_SC      	OR
             stActing.Holding_SC       	OR
             stActing.Unholding_SC     	OR
             stActing.Suspending_SC     OR
             stActing.Unsuspending_SC   OR
             stActing.Resetting_SC     	OR
             stActing.Completing_SC,
        PT := T#500MS); 
           
// State Complete if setSC is TRUE,
setSC := testSC.Q AND (stateLastCycie = actualState);

// This Statement MUST be written AFTER evaluation of setSC
stateLastCycie := actualState;
```

---

# PRG_Process
This program use the axes integrated in Pack but only for Execute and without **SC** **S**tate **C**omplete.

The Axes are already integrated in the Pack.

## Manual Jog
```iecst
(*
	Execute Manual Sequence
*)
IF PackTag.Status.StateCurrent = E_PackState.eExecute 	 AND
   (PackTag.Status.UnitModeCurrent = E_PackModes.Manual) THEN
	CASE eManualJog OF
	E_ManualJog.eIdle :
		IF PackTag.Status.UnitModeCurrent = E_PackModes.Manual THEN
			eManualJog := E_ManualJog.eNextMove;
		END_IF
```

## Automatic Sequence
```iecst
IF (PackTag.Status.StateCurrent = E_PackState.eExecute)      AND
   (PackTag.Status.UnitModeCurrent = E_PackModes.Production) THEN
	CASE eUnitMove OF
		  E_UnitMoveForPickAndPlace.Idle:
			(* Code for Idle state *)
			IF xNextStepEnable THEN
				eUnitMove := E_UnitMoveForPickAndPlace.InitMove;
			END_IF
```