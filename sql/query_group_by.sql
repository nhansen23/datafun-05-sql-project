SELECT Year, Sex as Gender, COUNT(DISTINCT ID) as Athlete_Count
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
GROUP BY Year, Gender
ORDER BY Year, Gender