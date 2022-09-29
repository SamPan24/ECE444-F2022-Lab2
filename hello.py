from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your UofT Email address?", validators=[DataRequired()])
    submit = SubmitField("Submit")

app = Flask(__name__, template_folder="/Users/SamPan 1/Documents/ECE444/Lab2-Flask/lab2_venv")
app.config["SECRET_KEY"] = "abcdefg"

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        old_email=session.get('email')
        
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session['name'] = form.name.data
        
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you have changed your email!")
        session['email'] = form.email.data
        
        new_email = form.email.data
        
        if "utoronto" in form.email.data:
            session["message"] = f"Your UofT email is {new_email}"
        else:
            session["message"] = "Please use an UofT email!"
        
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get("name"), message=session.get("message"))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


