import urllib.request
import urllib.parse
import json

if __name__ == '__main__':
    api = input('Please input API key:')
    with open('google.json', 'w', encoding='utf-8') as f:
        movies = []
        id_of_film = 1
        while id_of_film < 1001:
            url = 'https://api.themoviedb.org/3/movie/' + str(id_of_film)  + '?api_key=' + api + '&language=ru'
            try:
                data_of_film = json.loads(urllib.request.urlopen(url).read().decode('UTF-8'))
            except Exception:
                id_of_film += 1
            else:
                movies.append(data_of_film)
                id_of_film += 1
        json.dump(movies, f, ensure_ascii=False)
