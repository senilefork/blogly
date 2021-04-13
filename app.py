from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, PostTag, Tag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "super-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def list_users():
    """shows users in db"""
    users = User.query.all()
    tags = Tag.query.all()
    return render_template('base.html', users=users, tags=tags)

@app.route('/<int:user_id>')
def detail(user_id):
    user = User.query.get_or_404(user_id)
    #posts = Post.query.get_or_404(user_id).content
    
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
    return render_template('edit_form.html', user=user, posts=posts)

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

@app.route('/add_post/<int:user_id>')
def add_post_form(user_id):
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('add_post.html', user=user, tags=tags)

@app.route('/add_post/<int:user_id>', methods=["POST"])
def add_post(user_id):
    title = request.form["title"]
    content = request.form["post"]
    tags = request.form.getlist("tags")
    

    user = User.query.get_or_404(user_id)

    new_post = Post(title=title, content=content, user_id=user_id, tags=tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect('/')

@app.route('/post_detail/<int:post_id>')
def post_detail(post_id):

    post = Post.query.get_or_404(post_id)
    user_id = post.user_id
    user = User.query.get_or_404(user_id)

    return render_template('post_detail.html', post=post, user=user)

@app.route('/edit_post/<int:post_id>')
def edit_post_form(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template('edit_post.html', post=post)

@app.route('/edit_post/<int:post_id>', methods=["POST"])
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)
    title = request.form["title"]
    content = request.form["post"]

    post.edit_post(title,content)
    db.session.add(post)
    db.session.commit()

    return redirect('/')

@app.route('/delete_post/<int:post_id>', methods=["POST"])
def delete_post(post_id):

   post = Post.query.get_or_404(post_id)
   post.query.filter_by(id=post_id).delete()
   db.session.commit()

   return redirect('/')

@app.route('/tag_form')
def tag_form():
    return render_template('tag_form.html')

@app.route('/tag_form', methods=['POST'])
def tag():

    tag_input = request.form["tag"]
    new_tag = Tag(name=tag_input)
    db.session.add(new_tag)
    db.session.commit()
    
    return redirect('/')

@app.route('/edit_tags')
def edit_tags_form():
    tags = Tag.query.all()
    return render_template('edit_tags.html', tags=tags)

@app.route('/edit_tags', methods=["POST"])
def edit_tags():
    tag_ids = request.form.getlist("id")
    for id in tag_ids:
        tag = Tag.query.get_or_404(id)
        tag.query.filter_by(id=id).delete()
        db.session.commit()
    
    return redirect('/')





 

