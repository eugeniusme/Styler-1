import urllib.request
import urllib.parse
import json

def load_from_tmbd(id_of_film, api):
    url = 'https://api.themoviedb.org/3/movie/' + str(id_of_film)  + '?api_key=' + api + '&language=ru'
    return json.loads(urllib.request.urlopen(url).read().decode('UTF-8'))

if __name__ == '__main__':
    id_of_film = 215
    api = input('Please input key') 
    print('Budget of Saw II:', (load_from_tmbd(method='/movie/' + str(id_of_film), api_key=api)['budget']))
