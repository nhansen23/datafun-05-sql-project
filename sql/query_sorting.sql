SELECT Name as Athlete_Name, Year, country
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
ORDER BY Year DESC, country, Athlete_Name