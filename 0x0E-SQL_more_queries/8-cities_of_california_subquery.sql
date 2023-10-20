-- List cities of California
SELECT id, name
FROM cities
WHERE cities.state_id IN (SELECT id FROM states WHERE name = 'California');
ORDER BY id ASC;
