import sqlite3 as sql


def get_by_title(query_title):
    """
    Функция поиска фильмов в базе данных по названию
    """
    with sql.connect('netflix.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        query = (f"SELECT title, country, release_year, listed_in, description\n"
                 f"FROM netflix\n"
                 f"WHERE title LIKE '%{query_title}%'\n"
                 f"ORDER BY date_added DESC\n"
                 )
        cur.execute(query)
        query_result = cur.fetchone()
        result = None
        if query_result:
            result = {
                    "title": query_result["title"],
                    "country": query_result["country"],
                    "release_year": query_result["release_year"],
                    "genre": query_result["listed_in"],
                    "description": query_result["description"]
            }
        return result


def get_by_years(year_1, year_2):
    """
    Функция поиска фильмов в базе данных по годам выхода
    """
    with sql.connect('netflix.db') as con:
        result = []
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year_1} AND {year_2}
        LIMIT 100
        """
        cur.execute(query)
        query_result = cur.fetchall()
        for data in query_result:
            movie = {
                    "title": data["title"],
                    "release_year": data["release_year"],
            }
            result.append(movie)
        return result


def get_by_rating(rating_movie):
    """
    Функция поиска фильмов в базе данных по рейтингу
    """
    with sql.connect('netflix.db') as con:
        result = []
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating IN {rating_movie}
        LIMIT 100
        """
        cur.execute(query)
        query_result = cur.fetchall()
        for data in query_result:
            movie = {
                    "title": data["title"],
                    "rating": data["rating"],
                    "description": data["description"],
            }
            result.append(movie)
        return result


def get_by_genre(genre_movie):
    """
    Функция поиска фильмов в базе данных по жанру
    """
    with sql.connect('netflix.db') as con:
        result = []
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre_movie}%'
        ORDER BY release_year DESC
        LIMIT 10
        """
        cur.execute(query)
        query_result = cur.fetchall()
        for data in query_result:
            movie = {
                    "title": data["title"],
                    "description": data["description"],
            }
            result.append(movie)
        return result


def get_by_type(type_movie, release_year_movie, listed_in_movie):
    """
    Функция поиска фильмов в базе данных по данным типа фильма, года выпуска и жанра
    """
    with sql.connect('netflix.db') as con:
        result = []
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE type = {type_movie} AND release_year = {release_year_movie} AND listed_in LIKE '%{listed_in_movie}%'
        """
        cur.execute(query)
        query_result = cur.fetchall()
        for data in query_result:
            movie = {
                    "title": data["title"],
                    "description": data["description"],
            }
            result.append(movie)
        return result
