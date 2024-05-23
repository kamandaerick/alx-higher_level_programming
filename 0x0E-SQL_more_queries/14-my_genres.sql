-- list genres of the show Dexter
SELECT tv_genres.name  as name
FROM tv_genres
LEFT JOIN tv_shows ON tv_shows.id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
