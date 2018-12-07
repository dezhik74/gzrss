from app import app
from flask import render_template, flash
from time import sleep


def mysleep (sec):
    pass
#    sleep (sec)

@app.route('/')
@app.route('/index')
def index():
    name_of_master = "Сергей хозяин"
    flash('You were successfully logged in')
    return render_template('index.html', name = name_of_master)


@app.route('/serje')
def serje():
    return render_template('serje.html', foo=mysleep)

