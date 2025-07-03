# Documentation Pack ML (Siemens)
  ## 0. Legal info
  disclaimer
  ## 1. Présentation de la bibliothèque
Qu'est-ce qu'on trouve dans ce chapitre ?
### 1.1 Mode et états du pack ML
State machine diagram

Unit mode : Tableau _(description différent mode/vue de l'utilisateur, production, maintenance, userMode)_

States : Tableau _(description différent états/ bloc de la machine d'état)_

Control commands : Liste "bouton" affichage _???_

Changement d'état avec attribution de priorité _utilité??_
### 1.2 Hardware et software exigences
_équipements_

### 1.3 Ressources biblio
taille des FB (main, load and retain memory)
  ## 2. Définition des blocs de la biblio
  Qu'est-ce qu'on trouve dans ce chapitre ?
### 2.1 Lister les FB

### 2.2 Explication des FB
9x (ci-dessous pour un FB)

    - figure/schéma
    - principe des operations du bloc
    - Caractéristiques fonctionnelles (figure avec signal)
    - Paramètres input (nom, type, commentaires)
    - Paramètres output (nom, type, commentaires)
    - Affichages d'état et d'erreur
 PLC data types _pas compris_
 - typeConfiguration
 - typeDiagnostics
 - typeDiagnosticsEntry
 - typePackTags
 - typeAdmin
 - typeCommand
 - typeStatus
 - typeEvent
 - typeCommandIngredients
 - ...
  ## 3. Travailler avec biblio
Qu'est-ce qu'on trouve dans ce chapitre
### 3.1 Intégration de la biblio dans STEP 7

### 3.2 Intégration des blocs de bibliothèque dans STEP 7
  ## 4. Notes et support
Qu'est-ce qu'on trouve dans ce chapitre
_VIDE_
  ## 5. Appendix
Qu'est-ce qu'on trouve dans ce chapitre
### 5.1 Service and support
5x

    Entreprise/Nom de contact
    Pour quels services
    Mail de contact
### 5.2 Industry Mall
### 5.3 Application support
### 5.4 Links and literature
Topic
### 5.5 Change documentation
Version, modifications





---

----


# Documentation Pack ML (Bosch Rexroth)
## 1. Versions
## 2. Disclaimer
## 3. Installation guide
## 4. Intro et guide
figure/schéma (PackML Template : ISA-88 physical model)
## 5. Project structure
figure/schéma (PackML Template : Module Structure)
### 5.1 Prérequis
Logiciel
### 5.2 Structure générale PLC Code
### 5.3 PackML State Machine
Mode (liste)
State machine (figure/schéma)
Distinct State (liste)
Transition Commands (liste)
State (liste avec description)
### 5.4 CommandManager, CommandClient
- schéma du bloc UN, EM et CM
- Figure hiérarchie (UN, EM et CM)
  
## 5.5 Event, EventManager, EventAdministrator
Alarm, error, warning or message
## 5.6 Call tree

# 6. How To
    Très bon chapitre, pour expliquer comment créer nouveau EM
## 6.1 Add new Equipment Module (EM)
PRG : 
FB : 
## 6.2 Add new Control Module (CM)
PRG : 
FB : 
## 6.3 Add new mode

## 6.4 Implement mode in CM
## 6.5 Implement state in CM
## 6.6 Implement Event
## 6.7 Read active and acknowledged events
## 6.8 Add new axis
## 6.9 Switch states
## 6.10 Debug with internal visualization
Main 
Alarm
# 7. Utilities
## 7.1 EtherCAT
## 7.2 CtrlXDiagnostics
## 7.3 AccessRealTimeData
_ExampleReadRealTimeEtherCatData(PRG)
_ExampleReadRealTimeAxisDiag(PRG)
## 7.4 AxisDiagnostics
### 7.4.1 FB_InitAxisRTDiag
### 7.4.2 FB_EventAxis
## 7.5 DataTypes
## 7.6 ControlInformation
## 7.7 PackTags