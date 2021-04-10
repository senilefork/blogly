from models import User, db
from app import app

db.drop_all()
db.create_all()

user1 = User(first_name="Magic", last_name="Johnson", image_url="https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80")
user2 = User(first_name="Bob", last_name="Vila", image_url="https://images.unsplash.com/photo-1425082661705-1834bfd09dca?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1655&q=80")
user3 = User(first_name="Royce", last_name="Gracie", image_url="https://images.unsplash.com/photo-1497752531616-c3afd9760a11?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()
