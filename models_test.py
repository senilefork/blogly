from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_BATABASE_URI'] = 'postgresql:///users_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model for users"""

    def setUp(self):

        User.query.delete()

    def tearDown(self):

        db.session.rollback()
    
    def test_edit_user(self):
        user = User(first_name="TestFirst", last_name="TestLast", image_url="http://cats.com/cat.jpg")
        user.edit_user('Cool', 'MoD', 'http://dogs.com/dog.jpg')
        self.assertEquals(user.first_name, "Cool")
        self.assertEquals(user.last_name, 'MoD')
        self.assertEquals(user.url, 'http://dogs.com/dog.jpg')

