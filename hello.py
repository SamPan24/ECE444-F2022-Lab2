from flask import Flask

app = Flask(__name__)

@app.rout('/')
def index():
    return '<h1>Hello World!</h1>'
