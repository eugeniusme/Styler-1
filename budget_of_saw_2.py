import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {'api_key': api_key,
        'language': 'ru',}
    params.update(extra_params)
    return load_json_data_from_url(url, params)

if __name__ == '__main__':
    id_of_film = 215
    api = '319d54c2728dc4563bde29d5c4466336'
    print('Budget of Saw II:', (make_tmdb_api_request(method='/movie/' + str(id_of_film), api_key=api)['budget']))
