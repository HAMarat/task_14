import sqlite3 as sql


def get_by_title(query_title):
    with sql.connect('../task_14/netflix.db') as con:
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
        print(query_result)
        result = {
                "title": query_result["title"],
                "country": query_result["country"],
                "release_year": query_result["release_year"],
                "genre": query_result["listed_in"],
                "description": query_result["description"]
        }
        return result
