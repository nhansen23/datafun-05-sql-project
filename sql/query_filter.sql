-- Select all athletes and countries in the 2012 Olympics
SELECT DISTINCT athlete_id, athlete_name, country
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc
HAVING year = 2012