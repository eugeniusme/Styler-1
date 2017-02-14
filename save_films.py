import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


f = open('google.json', 'w', encoding='utf-8')
movies = []
i = 1
while i < 1001:
    try:
        righ = dict(make_tmdb_api_request(method='/movie/' + str(i), api_key='***'))
    except Exception:
        i += 1
    else:
        movies.append(righ)
        i += 1
json.dump(movies, f, ensure_ascii=False)
