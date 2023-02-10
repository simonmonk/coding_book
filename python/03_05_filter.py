movies = [
    {
        'title':'Jaws',
        'director':'Steven Spielberg',
        'duration': 124
    },
    {
        'title':'The Godfather',
        'director':'Francis Ford Coppola',
        'duration': 175
    },
    {
        'title':'Baby Driver',
        'director':'Edgar Wright',
        'duration': 115
    },
]

short_movies = []

for movie in movies:
    if movie['duration'] < 120:
        short_movies.append(movie)
        
print(short_movies)