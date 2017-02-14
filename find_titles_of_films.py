import json
import codecs

if __name__ == '__main__':
    with codecs.open('google.json', "r", encoding='utf-8') as f:
        movies = json.load(f)
    sub = input('Введите искомую подстроку: ')
    [print(movie['title']) for movie in movies if sub.lower() in movie['title'].lower()]
