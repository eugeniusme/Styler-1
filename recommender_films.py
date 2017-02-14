import json
import codecs

def existance_of_title(movies, myMovie):
    for movie in movies:
        if movie['title'] == myMovie:
            return movie
    return {}

def get_recommend(movies, inputMovie):
    recommend = {}
    genres = [film['name'] for film in inputMovie['genres']]
    for film in movies:
        if inputMovie['adult'] == film['adult']:
            genresFilm = [film['name'] for film in inputMovie['genres']]
            recommend[film['title']] = len(set(genres)&set(genresFilm)) * 10 + (10 - abs(film['vote_average'] - inputMovie['vote_average']))
    return recommend

def get_collection(movies, inputMovie):
    collection = []
    for film in movies:
        try:
            collectFilm = film['belongs_to_collection']['name']
            collectInputMovie = inputMovie['belongs_to_collection']['name']
        except TypeError:
            continue
        else:
            if collectFilm == collectInputMovie and inputMovie['title'] != film['title']:
                collection.append(film['title'])
    return collection

def print_recommend(collection, recommend, inputMovie):
    if len(collection) < 20:
        iter = len(collection)
        for keys, values in sorted(recommend.items(), key=lambda x: x[1], reverse=True):
            if keys not in collection and keys != inputMovie['title']:
                iter += 1
                collection.append(keys)
            if iter == 20:
                return collection
    else:
        return collection
    
if __name__ == '__main__':
    with codecs.open('google.json', "r", encoding='utf-8') as f:
        movies = json.load(f)

    myMovie = input('Введите название фильма: ')
    inputMovie = existance_of_title(movies, myMovie)
    if inputMovie == {}:
        print('Такого фильма в реестре нет. Программа завершилась.')
    else:
        genres = [film['name'] for film in inputMovie['genres']]
        collection = get_collection(movies, inputMovie)
        recommend = get_recommend(movies, inputMovie)
        print('Рекомендованные фильмы:')
        [print(i) for i in print_recommend(collection, recommend, inputMovie)]
