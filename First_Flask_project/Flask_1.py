from flask import Flask
from utils import string_html

app = Flask(__name__)


@app.route('/')
def view():
    return f'{string_html}'


app.run(debug=True, port=50000)
