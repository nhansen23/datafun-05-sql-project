SELECT year, gender, COUNTD(athlete_id) as athlete_count
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc
GROUP BY year, gender
ORDER BY year, gender