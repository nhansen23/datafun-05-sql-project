-- Count the number of athletes each Olympic year
SELECT year, COUNTD(athlete_id) as athlete_count
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc

-- Count the number of athletes per year per country
SELECT year, noc, country, COUNTD(athlete_id) as athlete_count
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc
ORDER BY year, athlete_count DESC

-- Count the number of athletes by gender each year
SELECT year, gender, COUNTD(athlete_id) as athlete_count
FROM athletes
INNER JOIN countries ON athletes.noc = countries.noc
ORDER BY gender, athlete_count DESC