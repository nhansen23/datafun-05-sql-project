-- Join athletes and countries
SELECT ID as Athlete_ID, Name as Athlete_Name, Sex as Gender, Age, Team, athletes.noc,
country, Games, Year, Season, Sport, Event, Medal
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc