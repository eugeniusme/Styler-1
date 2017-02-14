import json
import codecs

with codecs.open('google.json', "r", encoding='utf-8') as f:
    movies = json.load(f)

print('Введите название фильма:')
myMovie = input()
check=0
for movie in movies:
    if movie['title'] == myMovie:
        check = 1
        inputMovie = movie
        break
if check == 0:
    print('Такого фильма в реестре нет. Программа завершилась.')
    exit(0)
genres = [film['name'] for film in inputMovie['genres']]
collection = []
recommend = {}

for film in movies:
    if inputMovie['adult'] == film['adult']:
        genresFilm = [film['name'] for film in inputMovie['genres']]
        recommend[film['title']] = len(set(genres)&set(genresFilm)) * 10 + (10 - abs(film['vote_average'] - inputMovie['vote_average']))

    try:
        collectFilm = film['belongs_to_collection']['name']
        collectInputMovie = inputMovie['belongs_to_collection']['name']
    except TypeError:
        continue
    else:
        if collectFilm == collectInputMovie and inputMovie['title'] != film['title']:
            collection.append(film['title'])

print('Рекомендованные фильмы:')
if len(collection) < 20:
    [print(i) for i in collection]
    iter = len(collection)

    l = lambda x: x[1]
    for keys, values in sorted(recommend.items(), key=l, reverse=True):
        if keys not in collection and keys != inputMovie['title']:
            iter += 1
            print(keys)
        if iter == 20:
            break
else:
    [print(collection[i]) for i in range(10)]
