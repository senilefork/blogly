from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "super-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
#db.create_all()

@app.route('/')
def list_users():
    """shows users in db"""
    users = User.query.all()
    return render_template('base.html', users=users)

@app.route('/<int:user_id>')
def detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('detail.html', user=user)

@app.route('/add_user')
def add_user_form():
    return render_template('add_user.html')

@app.route('/add_user', methods=["POST"])
def add_user_to_db():
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    url = request.form["url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/edit_user/<int:user_id>')
def edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit_form.html', user=user)

@app.route('/edit_user/<int:user_id>', methods=["POST"])
def edit_user(user_id):
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    url = request.form["url"]

    user = User.query.get_or_404(user_id)
    user.edit_user(first_name, last_name, url)
    db.session.add(user)
    db.session.commit()
    return redirect('/')
    
@app.route('/delete/<int:user_id>', methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    user.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/')
