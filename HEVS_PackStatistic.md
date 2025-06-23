

# FB_PackStatistic

Certaines balises d'administration prennent en charge le transfert de données pour les calculs OEE. Reportez-vous à la norme **ISO 22400** pour obtenir des informations sur la mesure des indicateurs clés de performance (KPI), notamment l'OEE.


For each state
For each mode

Source of time
Use

```iecst
TYPE HEVS_Time :
STRUCT
	Date_and_time_in_seconds	: UDINT;
	Local_date_time_seconds 	: UDINT;
```
|=2^31-1	|bits|
|-----------|----|
|2147483647	|s|
|35791394	|min|
|596523	|h|
|24855	|j|
|68	|year|


Traduire en français les trucs ci-dessous.

## Admin.ModeTimeCurrent [Seconds]
-   Data Type: ``DINT``
-   Tag Descriptor: Current Mode Time
Current Mode Time
-   Unit of Measure: **Sec**

Cette balise représente la durée actuelle, **en secondes** passée **dans le mode actuel** comme indiqué par ``Status.UnitModeCurrent``. La valeur démarre à 0 à chaque changement de mode. Les valeurs passent à 0 après 2 147 483 647.

## Admin.StateTimeCurrent
-   Data Type: ``DINT``
-   Tag Descriptor: Current State Time
-   Unit of Measure: **sec**

Cette balise représente la durée actuelle, **en secondes** passée **dans l'état actuel** comme indiqué par ``Status.StateCurrent``. La valeur démarre à 0 à chaque fois que l'état est modifié. Les valeurs passent à 0 après 2 147 483 647.

## Admin.CumulativeTimes[#]
-   Data Type: CUMULATIVE_TIMES Array, User-defined array size, minimum 1
-   Tag Descriptor: Structured Array of Timer Values

Cette balise représente une collection de temps accumulé, **en secondes** passé dans n'importe quel état défini de n'importe quel mode défini. **L'utilisateur peut définir un nombre variable de collections de suivi du temps** indiquées par l'index du tableau et peut également définir quand les valeurs de temps dans chaque collection sont réinitialisées. L'étendue minimale du tableau est 1 ``Admin.CumulativeTimes[0]`` **noter l'index 0**.

> Dans cette implémentation, nous n'utilisons que ``Admin.CumulativeTimes[0]`` avec l'**index 0**.


## Admin.CumulativeTimes[#].AccTimeSinceReset
-	Data Type: ``DINT``
-	Tag Descriptor: Accumulated Time Since Last Reset
-	Unit of Measure: **Sec**

Dans l'implémentation de base, nous redémarrons le temps avec un reset du PLCm c'est à dire à chaque démarrage.

## Admin.CumulativeTimes[#].ModeStateTimes[#]
> Index. Pas de valeur, voir [Mode](#admincumulativetimesmodestatetimesmode) et [State](#admincumulativetimesmodestatetimesstate) ci-dessous.

## Admin.CumulativeTimes[#].ModeStateTimes[#].Mode
-	Data Type: ``DINT``
-	Tag Descriptor: Mode Time Values for each Mode
-	Unit of Measure: **Sec**

Cette balise représente la durée cumulée, **en secondes**, passée dans chaque mode depuis la dernière réinitialisation du minuteur et du compteur. Les valeurs reviennent à 0 après 2 147 483 647.

Dans notre implémentation, voir ``E_PackMode``.

## Admin.CumulativeTimes[#].ModeStateTimes[#].State[#]
-	Data Type: ``DINT`` Array
-	Tag Descriptor: State Time Values for each State in each Mode
-	Unit of Measure: **Sec**

Cette balise représente la durée cumulée, **en secondes**, passée dans chaque état d'un mode particulier depuis la dernière réinitialisation du minuteur et du compteur. L'index du tableau représente le numéro d'état tel que défini dans 4.3 et l'étendue du tableau est fixée à 18 [0..17]. Les valeurs passent à 0 après 2 147 483 647.

Dans notre implémentation, voir ``E_PackState``.