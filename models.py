from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(30),
                    nullable=False)
    last_name =  db.Column(db.String(30),
                    nullable=False)
    image_url = db.Column(db.Text)

    def edit_user(self, first_name, last_name, url):

        self.first_name = first_name
        self.last_name = last_name
        self.url = url

    posts = db.relationship("Post", backref="user")

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def edit_post(self, title, content):

        self.title = title
        self.content = content

    

    

    








