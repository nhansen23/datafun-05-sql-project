/*
-- Count the number of athletes each Olympic year
SELECT Year, COUNT(DISTINCT ID) as athlete_count
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
GROUP BY Year
*/

-- Count the number of athletes per year per country
SELECT Year, athletes.NOC, country, COUNT(DISTINCT ID) as Athlete_Count
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
GROUP BY Year, athletes.NOC, country
ORDER BY Year, Athlete_Count DESC

/*
-- Count the number of athletes by gender each year
SELECT Year, Sex as Gender, COUNT(DISTINCT ID) as Athlete_Count
FROM athletes
INNER JOIN countries ON athletes.NOC = countries.NOC
GROUP BY Year, Gender
ORDER BY Gender, Athlete_Count DESC
*/