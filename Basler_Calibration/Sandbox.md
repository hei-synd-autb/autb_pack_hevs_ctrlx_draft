# Creating an Object in JavaScript

To create an object in JavaScript, you can use the object literal syntax or the `new Object()` syntax. Here are examples of both:

## Using Object Literal Syntax

```javascript
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    occupation: "Developer"
};
```

## Using `new Object()` Syntax

```javascript
const person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 30;
person.occupation = "Developer";
```

Both methods create an object with the same properties and values.

plc/app/Application/sym/PRG_Sandbox/uliLoop

msg.topic = 'plc/app/Application/sym/PRG_Sandbox/uliLoop';

Je ne peux pas souscrire à une méthode.

Avec ce truc: cela fonctionne: diagnosis/get/actual/list

```iecst
{
    "listDiagnosisIdentificationWithTimestamp": [
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2002",
                "detailedDiagnosisNumber": "0C570106",
                "entity": "motion/axs/Axis_z"
            },
            "timestamp": "2025-01-09T16:15:13.818880Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2002",
                "detailedDiagnosisNumber": "0C570106",
                "entity": "motion/axs/Axis_y"
            },
            "timestamp": "2025-01-09T16:15:13.738835Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2002",
                "detailedDiagnosisNumber": "0C570106",
                "entity": "motion/axs/Axis_x"
            },
            "timestamp": "2025-01-09T16:15:13.738783Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2000",
                "detailedDiagnosisNumber": "0C550001",
                "entity": "motion/axs/Axis_x"
            },
            "timestamp": "2025-01-09T16:15:13.341449Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2000",
                "detailedDiagnosisNumber": "0C550001",
                "entity": "motion/axs/Axis_y"
            },
            "timestamp": "2025-01-09T16:15:13.341426Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "091F2000",
                "detailedDiagnosisNumber": "0C550001",
                "entity": "motion/axs/Axis_z"
            },
            "timestamp": "2025-01-09T16:15:13.341376Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "080E0540",
                "detailedDiagnosisNumber": "0C66003F",
                "entity": "health"
            },
            "timestamp": "2025-01-08T06:10:46.387728Z"
        },
        {
            "diagnosisIdentification": {
                "mainDiagnosisNumber": "080A0102",
                "detailedDiagnosisNumber": "00000000",
                "entity": "diagnosis/get/actual/list"
            },
            "timestamp": ""
        }
    ]
}

```