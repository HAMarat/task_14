from flask import Flask, jsonify
from utils import get_by_title, get_by_years, get_by_rating, get_by_genre

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route('/')
def start_page():
    """
    Вьюшка для стартовой страницы
    """
    return 'Start_page'


@app.route('/movie/<title>')
def return_by_title(title):
    """
    Вьюшка для поиска фильма по названию
    """
    result = get_by_title(title)
    if result:
        return jsonify(result)
    return f"Данные по запросу {title} не найдены"


@app.route('/movie/<int:year_1>/to/<int:year_2>')
def return_by_years(year_1, year_2):
    """
    Вьюшка для поиска фильмов по годам
    """
    result = get_by_years(year_1, year_2)
    if result:
        return jsonify(result)
    return "Данные по запросу не найдены"


@app.route('/rating/<rating>')
def return_by_rating(rating):
    """
    Вьюшка для поиска фильмов по категории
    """
    if rating == 'children':
        rating_movie = ('G', 'G')
    elif rating == 'family':
        rating_movie = ('G', 'PG', 'PG-13')
    elif rating == 'family':
        rating_movie = ('R', 'NC-17')
    else:
        return f"Данные по запросу {rating} не найдены"
    result = get_by_rating(rating_movie)
    return jsonify(result)


@app.route('/genre/<genre>')
def return_by_genre(genre):
    """
    Вьюшка для поиска фильмов по жанру
    """
    result = get_by_genre(genre)
    if result:
        return jsonify(result)
    return f"Данные по запросу {genre} не найдены"


@app.errorhandler(404)
def error_404(error):
    """
    Обработка ошибки 404
    """
    return "Страница не найдена", 404


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=9000)
