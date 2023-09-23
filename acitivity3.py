from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/') 
def index():
        return '<h1>Hello World!</h1>'

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html', name=name, currentTime=datetime.utcnow())
