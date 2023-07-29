select movie_titles.title, directors.name, movie_titles.duration
from movie_titles, directors
where movie_titles.duration > 120
and directors.id = movie_titles.director_id;