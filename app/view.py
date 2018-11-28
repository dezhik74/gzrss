from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name_of_master = "Сергей хозяин"
    return render_template('index.html', name = name_of_master)


@app.route('/serje')
def serje():
    return render_template('serje.html')

