-- Select all athletes and countries in the 2012 Olympics
SELECT Year, country, COUNT(DISTINCT ID) as Athlete_Count
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
HAVING COUNT(DISTINCT ID) > 15