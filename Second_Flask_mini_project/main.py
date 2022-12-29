from flask import Flask, render_template
from utilits import average


app = Flask(__name__)


@app.route('/')
def view():
    return render_template('home_page.html', height=average[0], weight=average[1])


app.run(debug=True, port=5000)
