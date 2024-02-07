SELECT athlete_name, year, country
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc
ORDER BY year DESC, country, athlete_name