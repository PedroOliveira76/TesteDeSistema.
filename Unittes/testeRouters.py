import unittest
from MaxMercado import app, database
from MaxMercado.models import Produto, Loginadm
from flask_testing import TestCase

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        database.create_all()

    def tearDown(self):
        database.session.remove()
        database.drop_all()

    def test_login_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assert200(response)
        self.assert_template_used('index.html')

    def test_produtos(self):
        response = self.client.get('/produtos', follow_redirects=True)
        self.assert200(response)
        self.assert_template_used('index.html')

    # Adicione mais testes conforme necessário

if __name__ == '__main__':
    unittest.main()
