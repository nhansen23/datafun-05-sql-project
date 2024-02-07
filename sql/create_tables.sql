-- Delete tables if they exist
-- Drop countries first as it depends on athletes

DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS athletes;


-- Create athletes table
-- No foreign keys

CREATE TABLE athletes (
    athlete_id TEXT PRIMARY KEY,
    athlete_name TEXT,
    gender TEXT,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    team TEXT,
    noc TEXT,
    games TEXT,
    year INTEGER,
    season TEXT,
    city TEXT,
    sport TEXT,
    event TEXT,
    medal TEXT
);

-- Create countries table
-- Foreign key noc
CREATE TABLE countries (
    noc TEXT PRIMARY KEY,
    country TEXT,
    notes TEXT,
    FOREIGN KEY (noc) REFERENCES athletes(noc)
);
