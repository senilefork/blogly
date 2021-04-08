from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_BATABASE_URI'] = 'postgresql:///users_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):

    def setUp(self):

        User.query.delete()

        user = User(first_name="Cool", last_name="MoD", image_url="http://dogs.com/dog.jp")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):

        db.session.rollback()

    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Cool", html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"firstname" : "Ro", "lastname" : "Jogan", "url" : "http://dogs.com/dog.jpg"}
            resp = client.post("/add_user", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<li><a href="/2">Ro</a></li>', html)

    def test_edit_user(self):
        with app.test_client() as client:
            d = {"firstname" : "Ned", "lastname" : "Flanders", "url" : "http://cats.com/cats.jpg"}
            resp = client.post(f"/edit_user/{self.user_id}", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<li><a href="/{(self.user_id)}">Ned</a></li>', html)

    def test_delete(self):
        with app.test_client() as client:
            resp = client.post(f"/delete/{self.user_id}", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            










