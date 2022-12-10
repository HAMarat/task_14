from flask import Flask, jsonify
from utils import get_by_title

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route('/')
def start_page():
    return 'Start_page'


@app.route('/<title>')
def return_by_title(title):
    result = get_by_title(title)
    return result


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=9000)
