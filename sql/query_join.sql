-- Join athletes and countries
SELECT athlete_id, athlete_name, gender, age, team, athlete.noc,
country, games, year, season, sport, event, medal
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc