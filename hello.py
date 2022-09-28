from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__, template_folder="/Users/SamPan 1/Documents/ECE444/Lab2-Flask/lab2_venv")

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html', name=name, current_time=datetime.utcnow())
