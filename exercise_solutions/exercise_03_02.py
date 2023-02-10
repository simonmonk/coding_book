movies = [
    {
        'title':'Jaws',
        'director':'Steven Spielberg',
        'duration': 124
    },
    {
        'title':'The Godfather',
        'director':'Francis Ford Coppola,',
        'duration': 175
    },
    {
        'title':'Baby Driver',
        'director':'Edgar Wright',
        'duration': 115
    },
]

for movie in movies:
    print(movie['title'] + ' (' + str(movie['duration']) + ' mins)')