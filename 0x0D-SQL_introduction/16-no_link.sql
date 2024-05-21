-- Select score and name froms econd_table where name is not null
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
