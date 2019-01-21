from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User, Incident, Script
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
import subprocess


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# @app.route("/incidents", methods=["GET", "POST"])
# def incidents():
#     if request.form:
#         name = Incident(name=request.form.get("name"))
#         description = Incident(description=request.form.get("description"))
#         status = Incident(status=request.form.get("status"))
#         timestamp = Incident(status=request.form.get("timestamp"))
#         db.session.add(name, description, status, timestamp)
#         db.session.commit()
#     return render_template("incidents.html")

@app.route('/incidents', methods=['GET', 'POST'])
def home():
    if request.form:
        try:
            name = request.form.get("name")
            description = request.form.get("description")
            status = request.form.get("status")
            print('chris this is', name, description, status)
            i = Incident(name,description,status)
            db.session.add(i)
            db.session.commit()
        except Exception as e:
            print("Failed to add incident")
            print(e)
    incidents = Incident.query.all()
    print('chris this incidents', incidents)
    return render_template("incidents.html", incident=incidents)

# @app.route("/incidents")
# def incidents1():
#     return render_template("incidents.html")

# @app.route("/update", methods=["POST"])
# def update():
#     newtitle = request.form.get("newtitle")
#     oldtitle = request.form.get("oldtitle")
#     book = Book.query.filter_by(title=oldtitle).first()
#     book.title = newtitle
#     db.session.commit()
#     return redirect("/")

@app.route("/update", methods=["POST"])
def update():
    try:
        newincidentname = request.form.get("newincidentname")
        oldincidentname = request.form.get("oldincidentname")
        print('chris old', oldincidentname, 'chris new', newincidentname)
        incident = Incident.query.filter_by(name=oldincidentname).first()
        incident.name = newincidentname
        db.session.commit()
    except Exception as e:
        print("Couldn't update Incident")
        print(e)
    return redirect("/incidents")


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    print('chris this name: ', name)
    i = Incident.query.filter_by(name=name).first()
    print('chris this i,', i)
    db.session.delete(i)
    db.session.commit()
    return redirect("/incidents")

# @app.route('/upload')
# def show_all_scripts():
#     ls = subprocess.check_output(['ls', 'app/axis'])
#     print(ls)
#     list = ls.split('\n')
#     print(list)
#
#     return render_template('scripts.html', list=list)

# ADDING SCRIPTS
@app.route('/upload', methods=['GET', 'POST'])
def scripts():
    if request.form:
        try:
            uploaded_file = request.form.get("script_name")
            description = request.form.get("description")
            parameters = request.form.get("parameters")
            documentation = request.form.get("documentation")

            script = Script(uploaded_file, description, parameters, documentation)
            db.session.add(script)
            db.session.commit()
        except Exception as e:
            print("Failed to add script")
            print(e)
    scripts = Script.query.all()

    return render_template("scripts.html", scripts=scripts)

# Update Scripts
@app.route("/update_scripts", methods=["POST"])
def update_scripts():
    try:
        new_script_name = request.form.get("new_script_name")
        old_script_name = request.form.get("old_script_name")
        print('chris old', old_script_name, 'chris new', old_script_name)
        script = Script.query.filter_by(name=old_script_name).first()
        script.name = new_script_name
        db.session.commit()
    except Exception as e:
        print("Couldn't update Script")
        print(e)
    return redirect("/upload")

@app.route("/delete_scripts", methods=["POST"])
def delete_scripts():
    name = request.form.get("script_name")
    i = Script.query.filter_by(name=name).first()
    db.session.delete(i)
    db.session.commit()
    return redirect("/upload")

