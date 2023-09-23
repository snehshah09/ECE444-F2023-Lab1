from flask import Flask, render_template, session, redirect, url_for, flash 
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField 
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yooo'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) 
    Email = EmailField('What is your uoft email?', validators=[DataRequired(), Email()]) 
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
         old_name = session.get('name')
         old_email = session.get('email')
         if old_name is not None and old_name != form.name.data:
             flash('Looks like you have changed your name!')
         session['name'] = form.name.data
         if old_email is not None and old_email != form.Email.data:
             flash('Looks like you have changed your email!')
         session['email'] = form.Email.data

         if session.get('email').find('utoronto') == -1:
             session['email'] = 'wrong-email'
             
         return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get("email"))

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())
