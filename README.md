# Styler-1


# budget_of_saw_2.py
Скрипт выводит бюджет фильма "Пила 2" (id в TMBD 215).

Входные данные: TMBD АПИ ключ.

Выходные данные: бюджет фильма с id 215 (в данном случае "Пила 2").


# save_films.py
Скрипт скачивает из TMBD данные о первых 1000 фильмов и сохраняет всю информацию в файл google.json.

Входные данные: TMBD АПИ ключ.

Выходные данные: файл google.json с базой фильмов.


# find_titles_of_films.py
Скрипт ищет введенное слово (подстроку) в названиях фильмов во всей базе, и выводит их названия, если данная построка содержится в них.

Входные данные: подстрока, по которой будет проведен поиск.

Выходные данные: названия фильмов, содержащих построку.


# recommender_films.py
Скрипт после ввода названия фильма формирует рекомендованные к просмотру картины. Сходства определяются по вхождению в одну коллекцию, похожим жанрам, рейтингу и одинаковому возрастному ошграничению.

Входные данные: название фильма, по которому пользователь хочет получить рекомендации.

Выходные данные: рекомендованные к просмотру фильмы.
