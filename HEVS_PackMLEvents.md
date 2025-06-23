# Ce document sert de base au cours sur les alarmes.

Objectif, comprendre les alarmes, les utiliser et les mettre à disposition des utilisateurs.

Nous allons séparer globalement les alarmes en deux catégories.

# Maintenance
Celle qui sont utile à la maintenance et au diagnostic de la machine par le personnel de maintenance, voir à l’éditeur du programme.

# Operation
Celles qui sont utiles à l’opérateur.
Pour celles qui sont utiles à l’opérateur, nous allons nous référer à la liste des alarmes selon PackML.

## Règles principales de la gestion des alarmes pour l'opérateur.

> Chaque alarme est unique pour la machine.

> La liste des alarmes est connues.

De fait, il n'est pas nécessaire de prévoir une allocation dynamique des alarmes. On peut utiliser un paramètre fixe pour le nombre d'alarmes, ci-dessous **#**.

# EVENT
Correspond à la collection de balises nécessaires pour capturer les événements de la machine tels que les alarmes, les avertissements ou d'autres événements.

```iecst
TYPE EVENT :
STRUCT
	Trigger		: BOOL;
	ID			: DINT:
	Value		: DINT;
	Message		: STRING;
	Category	: DINT;
	DateTime	: DATE_AND_TIME;
	AckDateTime	: DATE_AND_TIME;
END_STRUCT
END_TYPE
```
## Les EVENT selon PackML.

> Selon analyse TR88 2022, 7.5.3.7 Admin.AlarmHistory[#], les ID des alarmes commencent à 0.

``Admin.Alarm[#]``

-   Data Type: ``EVENT`` Array
-   Descriptor: Array of Given Size for Machine Alarms

Les balises d'alarme associées à l'interface locale sont généralement utilisées comme paramètres affichés ou utilisés sur l'unité localement, par exemple à partir d'une IHM. Ces paramètres d'alarme peuvent être utilisés pour afficher toute alarme ou cause d'arrêt de la machine qui se produit actuellement dans le système. Les alarmes sont généralement limitées à l'unité de la machine. L'étendue du tableau correspond au nombre maximal d'alarmes devant être émises.

``Admin.Alarm[#].Trigger``
-   Data Type: ``BOOL``
-   Tag Descriptor: Alarm Message Trigger

Le déclencheur d'alarme doit être activé uniquement lorsque **l'alarme est actuellement active**.

``Admin.Alarm[#].ID``

-   Data Type: ``DINT``
-   Tag Descriptor: Alarm Message Identification Number

Le numéro d’identification d’alarme est une valeur **unique** attribuée à chaque alarme.

``Admin.Alarm[#].Value``

-   Data Type: DINT
-   Tag Descriptor: Alarm Message Number

Le numéro du message d'alarme est une valeur associée à l'alarme permettant d'obtenir des détails spécifiques à l'utilisateur ou de décomposer l'**Alarm.ID** de manière plus détaillée.

> C'est pour cette raison que l'alarme ne peut pas simplement résulter de la valeur de  **#**.

> L'unicité de l'alarme est la combinaison de **ID et Valeur**.

Exemple:

-   ID = 3
-   Valeur = 1
-   Message = *Gripper error, not closed*

-   ID = 3
-   Valeur = 2
-   Message = *Gripper error, not open*



``Admin.Alarm[#].Message``
-   Data Type: ``STRING``
-   Tag Descriptor: Alarm Message

The alarm message is the actual text of the alarm for those machines capable of providing string information.

``Admin.Alarm[#].Category``
-   Data Type: ``DINT``
-   Tag Descriptor: Alarm Category

La catégorie d'alarme permet de regrouper les alarmes en niveaux de réponse qui peuvent être utilisés **pour émettre des commandes d'état**, afficher des informations sur une HMI ou effectuer d'autres actions. Par exemple, les alarmes de la catégorie 0 peuvent être uniquement d'affichage HMI, les alarmes de la catégorie 1 peuvent déclencher une commande d'abandon, etc.

En se basant sur les commandes de PackML, nous aurons les catégories suivantes:

|Command    | Category  | Need Clear |
|-----------|-----------|------------|
|Suspend    |1          |No          |
|Hold       |2          |Yes         |
|Stop       |3          |Yes         |
|Abort      |4          |Yes         |
|Complete   |6          |Yes         |
|           |           |            |
|Warning    |0          |No          |

> **Complete**, here we suppose that the machine can be stopped, no because of a kind of error, but simply because the production is completed.

La principale différence entre Hold et Suspend, c'est qu'avec un Suspend, la machine peut redémarrer automatiquement une fois la condition externe de blocage résolue.

> Exemple: une machine de remplissage de bouteilles attend des bouteilles en entrée.

``Admin.Alarm[#].DateTime``
-   Data Type: ``DATE_TIME``
-   Tag Descriptor: Date and Time the Alarm Occurred

L'horodatage du moment où l'alarme a été déclenchée pour la première fois.

``Admin.Alarm[#].AckDateTime``
-   Data Type: ``DATE_TIME``
-   Tag Descriptor: Date and Time the Alarm was Acknowledged

L'horodatage du moment où l'alarme a été reconnue par l'opérateur ou effacée.

``Admin.AlarmExtent``
-   Data Type: ``DINT``
-   Tag Descriptor: Extent of Alarm Array

L'étendue de l'alarme est associée au nombre maximal d'alarmes nécessaires pour l'annonce ou la création de rapports de la machine. Cette balise peut être utilisée par une machine distante

> On peut considérer cette valeur comme la taille du tableau d'alarmes.

## Commentaire (pour avancer)
On voit que dans Alarm, il y a Trigger.
Donc, chaque alarme de Admin.Alarm peut être utilisée directement.

Les systèmes de gestion d'alarmes de différents fabricants permettent une multitude de combinaison pour s'adapter à chaque type d'utilisation, qui n'est pas nécessairement liée au PackML.

Si l'on se contente du packML on peut partir sur une quantité relativement limitée d'alarmes.

Le cas des axes numériques est un bon exemple particulier. Si l'on se réfère à la documentation des axes, on verra que chaque axe contient une grande quantité d'alarmes. 

Le mieux est de faire un tableau.

|# |Trigger    |ID |Value|Message                    |Category|DateTime|AckDateTime|
|--|-----------|---|-----|---------------------------|--------|--------|-----------|
|1 |FALSE      |1  |1    |Stop, Gripper Not Closed   |3       |12h23   |12h37      |
|2 |FALSE      |1  |2    |Stop, Gripper Not Open     |3       |        |           |
|3 |FALSE      |1  |3    |Stop, Gripper State Unknown|3       |        |           |
|4 |FALSE      |1  |4    |Hold, Gripper Not Closed   |2       |        |           |
|5 |FALSE      |1  |5    |Hold, Gripper Not Open     |2       |        |           |
|6 |FALSE      |1  |6    |Hold, Gripper State Unknown|2       |        |           |
|7 |FALSE      |2  |1    |Abort E-Stop pressed       |4       |        |           |
|8 |FALSE      |3  |1    |Abort Axis Not in position |4       |        |           |
|9 |FALSE      |3  |2    |Stop Axis Not in position  |3       |        |           |
|10|FALSE      |3  |3    |Hold Axis Not in position  |2       |        |           |

>Commentaires sur le tableau
-   Le grandeurs **value** sont différentes pour une fonction Stop ou une fonction Hold.
-   Le E-Stop passe par un relais de sécurité avec un délais sécurisé. Cela permet d'arrêter proprement certains éléments avant que le relais de sécurité ne force, par exemple, la coupure d'alimentation électrique.
-   Les ID sont regroupés par type de fonction.
-   On pourrait aussi choisir de regrouper les ID par catégorie.

> Le message sera susceptible d'être complété.

|3 |1 |Abort Axis Error, **Axis X**|15h31|15h56|

# Alarm History

``Admin.AlarmHistory[#]``
-   Data Type: ``EVENT`` Array
-   Tag Descriptor: Array of Given Size for Machine Fault Number and Messaging History

Le tableau **AlarmHistory** est réservé aux alarmes qui se sont produites sur l'unité/machine et peut être trié par ordre chronologique, l'alarme la plus récente étant indexée sous la forme Admin.AlarmHistory **[0]**. L'étendue du tableau correspond au nombre maximal d'alarmes historiques devant être conservées **pour une visualisation ultérieure**.

Tous les éléments inutilisés doivent être définis sur des valeurs nulles (zéro)

> En d'autres termes, c'est le **log** des alarmes.

Pour le reste, le tableau AlarmHistory contient le même type d'information que ``Alarm[#]``.

``Admin.StopReason``
-   Data Type: ``EVENT``
-   Tag Descriptor: Machine Stop Reason is typically used for *First Out Fault* Reporting and Other Stoppage Events. The stop reason is the first event captured during an **abort**, **hold**, **suspend**, or **stop** event.

> D'une certaine manière, ce Descriptor définit très clairement ce que sont les alarmes. Des événements qui génèrent une des commandes suivantes: **abort**, **hold**, **suspend**, or **stop**.

*Le document de référence comporte une erreur dans la définition de StopReason. Il confon état et commande. Ce document est corrigé.*

Les tags suivants corresponds aux autres tags de EVENT. Sans commentaire nécessaire.

Pour une utilisation simplifiée d'un système de gestion des alarmes selon PackML, on pourrait se contenter de n'afficher que StopReason.

# Warning
``Admin.Warning[#]``
-   Data Type: ``EVENT`` Array
-   Tag Descriptor: Machine warnings are for general events that do not cause the machine to stop, but may require operator action as a stoppage may be imminent. **Warnings are not typically stored in history**.


# Exemple de numéros d'alarme Rexroth
**080F0300** Security: Error in certificate management
For the exact cause and remedy, refer to the respective detailed diagnostics.
## Detailed diagnostics
-   **0C7A0061**
-   **0C7A0062**
-   **0C7A0063**

## Diagnostic class, bits 19-16
Defines the class and thus the type of the main diagnostics
Chez Rexroth, les numéros d'alarmes contiennent le type d'alarme

### 0xA Message
-   **Use**: Information on operating states or other information
-   **Example**: e.g. "Booting completed", "Application download completed"
### 0xE Warning
-   **Use**: Warning against specific states in the system
-   **Example**: e.g. "Temperature warning", "Hard disk memory at minimum"
### 0xF Errors
-   **Use**: Reporting an error on specific states in the system
-   **Example**: e.g. "Maximum temperature exceeded - System shutdown", "General error of the axis"
### Other
-   Reserved

> Chez Rexroth, l'unicité dépend de l'ID, puis éventuellement du diagnostic détaillé. On comprend dans ce cas particulier que l'action, commande, que peux provoquer une alarme est unique. Les bits 19-16 réservés dans le message de 32 bits ne peuvent provoquer autre chose que ce pour quoi il sont conçus.

## Source type, bits 29-24

### 0x0E OEM machine-specific
-   **Use**: To be used only by the OEM customer to create individual diagnostics
-   **Example**: Machine-specific application of an OEM

### 0x0F OEM machine-HMI application
-   **Use**: To be used only by the OEM customer to create individual diagnostics
-   **Example**: Visualization of the OEM managing the machine

> Les numéros disponibles par le contstructeur de machine, puis le cas échéant par l'utilisateur final sont clairement définis. Cela évite un risque de conflit avec les autres modules de Rexroth, ou par exemple des partenaire fournisseurs de librairies, par exemple HD Vision Systems.

# Remarques de codage
Le principe de fonctionnement est repris directement de la description de [Schneider Electric FC_SetAlarm](https://product-help.schneider-electric.com/Machine%20Expert/V1.1/en/PackMLli/PackMLli/PackMLLb_Functions/PackMLLb_Functions-7.htm) et [FC_SetWarning](https://product-help.schneider-electric.com/Machine%20Expert/V1.1/fr/PackMLli/PackMLli/PackMLLb_Functions/PackMLLb_Functions-8.htm#XREF_D_SE_0078016_1).

Le codage est propre à la HEVS
Quelques différences

Il serait bien de mettre des trigger sur les set et ack (pas encore fait ou teter)

La sortie diNumberOfActive.. n'existe pas.

Les variables de temps sont écrites sur la structure en paramètre au moment de l'existence de l'alarme, pas au moment de son traitement dans le FB.

# Tests
Au moment de l'écriture de ce document, testé sur TwinCAT avec 3 alarmes.

# FB_HEVS_SetAlarm
> Do **NOT** used Alarm ID = 0.

Pour l'instant, sous forme de FB pour la facilité des debug.
Pourrait passer en fonction.
Aucun code propre à TwinCAT, devrait fonctionner avec n'importe quel Codesys

## History
Juste avant d'être effacée de la liste des alarmes, l'alarme est enregistrée dans AlarmHistory.
Ce mode de faire permet d'attendre le dernier moment pour prendre en compte l'acknowledge dans l'historique. 

## Taille de l'historique
La conception du buffer de l'historique le laisse en mémoire vive, il est conçu pour une visualisation simple, mais par pour un diagnostic à plus long terme.
Rester dans l'ordre de grandeur d'une vingtaine de valeur.

Pour une sauvegarde plus complexe, on passera par le système spécifique de diagnostic de la plateforme (e.g. Library Twincat Tc3_EventLogger, Library CtrlX Core CXAC_Diagnostics)

# FB_HEVS_SetWarning
> Do **NOT** used Warning ID = 0.

Ces deux FB avec la structure PackTAG permet de gérer un système simple d'alarmes indépendament du hardware.

On pourra si nécessaire les compléter pour utiliser les systèmes de log complets propres aux différents fournisseurs

# Multitasking
Warning, the implementation of these alarms is basic. It has not been tester for execution in multiple tasks

# FB_HEVS_StopReason
This FB is used to write in Admin.StopReason.

> TR 88 not precise, we will show the Cmd with the Highest Priority with Abort, the higest, Stop, Complete, Hold and Suspend, the lowest.

> Comme les commandes de rang inférieur perdent leur sens en cas de présence de commande de rang supérieur, seule la commande de rang la plus haute sera représentée dans la sortie en BOOL;

As A Stop depends of the Pack Commands Suspend, Hold, Stop or Abort, it is a little bit specific.
Here, the FB_HEVS_StopReason receive for parameters to define the Category which stops the machine.

SuspendCategoy		Default 1
HoldCategoy			Default 2
StopCategoy			Default 4
AbortCategoy		Default 4

CompleteCategory	Default 6

``Admin.StopReason``
	Data Type: ``EVENT``
	Tag Descriptor: Machine Stop Reason is typically used for *First Out Fault* Reporting and Other Stoppage Events. The stop reason is the first event captured during an abort, held, suspended, or stop event.

``Admin.StopReason.Trigger``
-	Data Type: ``BOOL``
-	Tag Descriptor: Stop Reason Message Trigger

Le déclencheur de raison d'arrêt doit être activé **uniquement lorsque la raison d'arrêt est actuellement active**.

``Admin.StopReason.ID``
-	Data Type: ``DINT``
-	Tag Descriptor: Stop Reason Message Identification Number

Le numéro d'identification de la raison d'arrêt est une valeur unique attribuée à chaque raison d'arrêt.

``Admin.StopReason.Value
-	Data Type: ``DINT``
-	Tag Descriptor: Stop Reason Value

Le numéro de valeur de raison d'arrêt est une valeur associée à la raison d'arrêt permettant des détails spécifiques à l'utilisateur ou de décomposer le StopReason.ID de manière plus détaillée.

``Admin.StopReason.Message``
-	Data Type: ``STRING``
-	Tag Descriptor: Stop Reason Message

Le message de raison d'arrêt est le texte réel de la raison d'arrêt pour les machines capables de fournir des informations de chaîne.

``Admin.StopReason.Category``
-	Data Type: ``DINT``
-	Tag Descriptor: Stop Reason Category

Stop Reason category is used to report the response level of **the event that caused production to cease**. *See Completed too*

``Admin.StopReason.DateTime``
-	Data Type: ``DATE_TIME``
-	Tag Descriptor: Date and Time the Stop Reason Occurred

L'horodatage du moment où la raison de l'arrêt a été déclenchée pour la première fois.

``Admin. StopReason.AckDateTime``
-	Data Type: ``DATE_TIME``
-	Tag Descriptor: Date and Time the Stop Reason was Acknowledged

L'horodatage du moment où la raison de l'arrêt a été reconnue par l'opérateur ou effacée.