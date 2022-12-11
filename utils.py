import sqlite3 as sql


def get_by_title(query_title):
    with sql.connect('netflix.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title LIKE '%{query_title}%'
        ORDER BY date_added DESC
        """
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


def get_by_type(type, release_year, listed_in):
    with sql.connect('netflix.db') as con:
        result = []
        con.row_factory = sql.Row
        cur = con.cursor()
        query = f"""
        SELECT title, release_year, listed_in
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
