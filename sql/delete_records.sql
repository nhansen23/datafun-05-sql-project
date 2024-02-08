-- Delete records from countries table where the country field is null
DELETE FROM countries
WHERE country = '' OR country IS NULL;
