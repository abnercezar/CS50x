SELECT AVG(rating) AS avg_ratings FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE year = 2012;