import json

s = '{"title": "Jaws", "director": "Steven Spielberg", "duration": 124}'

dict = json.loads(s)

print(dict['title'])