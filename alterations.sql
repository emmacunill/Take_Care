CREATE DATABASE IF NOT EXISTS final_project;
use final_project;

ALTER TABLE emsemotions
MODIFY COLUMN date DATE,
MODIFY COLUMN time TIME;

ALTER TABLE daylyemotions
MODIFY COLUMN date DATE;

ALTER TABLE fdf
MODIFY COLUMN date DATE,
MODIFY COLUMN time TIME;

ALTER TABLE pdef
MODIFY COLUMN date DATE,
MODIFY COLUMN time TIME;


ALTER TABLE monthlyemotions
MODIFY COLUMN month VARCHAR(10);
UPDATE monthlyemotions
SET month = STR_TO_DATE(CONCAT(month, '-01'), '%Y-%m-%d');


ALTER TABLE weeklyemotions
MODIFY COLUMN week VARCHAR(10);

UPDATE weeklyemotions
SET week = STR_TO_DATE(CONCAT(SUBSTRING(week, 1, 4), '-01-01'), '%Y-%m-%d') + INTERVAL SUBSTRING(week, 6, 2) - 1 WEEK;


    






