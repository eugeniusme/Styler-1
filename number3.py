import json
import codecs

with codecs.open('google.json', "r", encoding='utf-8') as f:
    movies = json.load(f)

print('Введите искомую подстроку:')
sub = input()
[print(movie['title']) for movie in movies if sub.lower() in movie['title'].lower()]

