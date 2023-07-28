-- Get all comedy movies
SELECT
    TV_SHOWS.TITLE
FROM
    TV_SHOWS
    JOIN TV_SHOW_GENRES
    ON TV_SHOWS.ID = TV_SHOW_GENRES.SHOW_ID JOIN TV_GENRES
    ON TV_GENRES.ID = TV_SHOW_GENRES.GENRE_ID
WHERE
    TV_GENRES.NAME = 'Comedy'
ORDER BY
    TV_SHOWS.TITLE;