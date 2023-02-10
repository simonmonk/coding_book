# run from same directory as test_db.sqlite3

import sqlite3
connection = sqlite3.connect('test_db.sqlite3')
cursor = connection.cursor()

for row in cursor.execute('SELECT id, name FROM directors'):
    id, name = row
    movies_cursor = connection.cursor()
    movies_cursor.execute('SELECT COUNT(*) FROM movie_titles WHERE director_id = ' + str(id))
    movies_count = movies_cursor.fetchone()[0]
    print(name + " " + str(movies_count))