import unittest
from Items import create_app, db
from Items.models import User
from tests import TestConfig


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='john')
        u.set_password('pass1234')
        self.assertTrue(u.check_password('pass1234'))
        self.assertFalse(u.check_password('123456'))