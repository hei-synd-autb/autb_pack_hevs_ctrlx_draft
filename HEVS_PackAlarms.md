<h1 align="left">
  <br>
  <img src="./img/hei-en.png" alt="HEI-Vs Logo" width="350">
  <br>
  HEI-Vs Engineering School
  <br>
</h1>

# HEVS Pack Events

> There are two type of Events. [Alarms](#fb_hevs_setalarm) and [Warnings](#fb_hevs_setwarning).

> Note about first index. **0 or 1** ? It can be found in TR88 2022, something like that : *The AlarmHistory array is reserved for alarms that have occurred on the unit/machine and can be sorted in chronological order with the most recently occurring alarmed indexed as Admin.AlarmHistory[0].*

**It is clear, First index is 0**.

## About HEVS Pack Alarm
Except for the functions of Date and Time, we use only Codesys standard libraries, it should be no problems of portability. We have made transfer of code from CtrlX core to TwinCAT 3 and vice versa using PLCopen XML file format without problems.
Portability to Simatic could be a problem, because we make an intensive use of ``ENUM``. You could replace ``ENUM`` with constants. Please **do not use cardinal numbers** when writing ``CASE..OF``, **This is a very bad programming style!**  

## Link to internal log.
If you need a more sophisticated log system for alarms, you could use for exemple TwinCAT Tc3_EventLogger library or Rexroth CXAC_Diagnostics library or other to complete your code. The **advantage of our library** is that is easy to access using for example OPC UA tool or low code UI tools like NodeRED.

## Bigest advantage of our implementation.
100% open.

# Function Blocks for alarm management.

## FB_

### HEVS_PackTag_Event
Is TR88 2022 EVENT.

```iecst
TYPE HEVS_PackTag_Event :
STRUCT
	Trigger			: BOOL;
	ID				: DINT;
	Value			: DINT;
	Message			: STRING;
	Category		: DINT;
	DateTime		: DATE_AND_TIME;
	AckDateTime		: DATE_AND_TIME;
END_STRUCT
END_TYPE

```

# FB_HEVS_SetWarning

## Header of SetWarning
```iecst
FUNCTION_BLOCK FB_HEVS_SetWarning
VAR_INPUT
	// Active on state
	bSetWarning					: BOOL := FALSE;
	// Active on rising edge
	bAckWarningTrig				: BOOL := FALSE;
	// Event Configuration
	ID							: DINT;
	Value						: DINT;
	Message						: STRING;
	Category					: DINT;	
END_VAR
VAR_IN_OUT
	// Base time from PackTag.Admin.PLCDateTime
	// PackTag.Admin.PLCDateTime should be set depending of HW system
	plcDateTimePack				: DATE_AND_TIME;
	// A reference to list of Warnings from GVL PackTag
	stAdminWarning				: ARRAY[0..HEVS_PackTag_GVL.C_ADMIN_MAXWARNINGS] OF HEVS_PackTag_Event;
END_VAR
VAR_OUTPUT
	bMaxNbOfAlarmReached		: BOOL;
	stErrorString				: STRING;
END_VAR
```

## Use of SetWarning

```iecst
// Instance
fbSetWarning_0	: FB_HEVS_SetWarning;

(*----------------------------------------------------------------------------*)

// Call
fbSetWarning_0(bSetWarning := PackTag.hevsPackAlarm_UI.uiSetWarning_0,
	           bAckWarningTrig := PackTag.hevsPackAlarm_UI.uiAckWarning_0,
			   // Warning Parameters
			   ID := 1,
	           Value := 31,
	           Message := 'Warning 0, Door Open',
	           Category := E_EventCategory.Warning,
			   // Reference to plc time from PackTag
			   plcDateTimePack	:= PackTag.Admin.PLCDateTime,
			   // Link to PackTag Admin
	           stAdminWarning := PackTag.Admin.Warning);
```

# FB_HEVS_SetAlarm

## Header of SetAlarm

```iecst
VAR_INPUT
	// Active on state
	bSetAlarm					: BOOL := FALSE;
	// Active on rising edge
	bAckAlarmTrig				: BOOL := FALSE;
	// Event Configuration
	ID							: DINT;
	Value						: DINT;
	Message						: STRING;
	Category					: DINT;
END_VAR
VAR_IN_OUT
	// Base time from PackTag.Admin.PLCDateTime
	// PackTag.Admin.PLCDateTime should be set depending of HW system
	plcDateTimePack				: DATE_AND_TIME;
	// A reference to Alarm and Alarm History of PackTag.
	stAdminAlarm				: ARRAY[0..HEVS_PackTag_GVL.C_ADMIN_MAXALARMS] OF HEVS_PackTag_Event;
	stAdminAlarmHistory  		: ARRAY[0..HEVS_PackTag_GVL.C_ADMIN_MAXHISTORYALARMS] OF HEVS_PackTag_Event;
END_VAR
VAR_OUTPUT
	bMaxNbOfAlarmReached		: BOOL;
	stErrorString				: STRING;
END_VAR
```

## Use of SetAlarm 

```iecst
// Instance of FB_HEVS_SetAlarm
fbSetAlarm_0	 : FB_HEVS_SetAlarm;

(*----------------------------------------------------------------------------*)

// Call of fbSetAlarm_0
fbSetAlarm_0(// Bit activation of Alarm and Ack
			 bSetAlarm := PackTag.hevsPackAlarm_UI.uiSetAlarm_0,
	         bAckAlarmTrig := PackTag.hevsPackAlarm_UI.uiAckAlarm_0,
			 // Alarm Parameters
			 ID := 5,
	         Value := 35,
	         Message := 'Abort 4, E-Stop',
	         Category := E_EventCategory.Abort,
			 // Reference to plc time from PackTag
			 plcDateTimePack	:= PackTag.Admin.PLCDateTime,
			 // Link to PackTag Admin
	         stAdminAlarm := PackTag.Admin.Alarm,
			 stAdminAlarmHistory := PackTag.Admin.AlarmHistory);

```

## FB_HEVS_StopReason

### Output stopReasonToMaster
This output is in format ``E_PackCmd``, DINT.
This output is intended to send Stop Commands from Alarms to ``FB_PackMasterState``.

```iecst
TYPE E_PackCmd :
(
	eUndefined := 0,
	eReset := 1,
	eStart := 2,
	eStop := 3,
	eHold := 4,
	eUnhold := 5,
	eSuspend := 6,
	eUnsuspend := 7,
	eAbort := 8,
	eClear := 9,
	eComplete := 10
) DINT;
END_TYPE
```

