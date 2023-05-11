import unittest
from MaxMercado import app, database
from MaxMercado.models import Produto, Loginadm

class TestModels(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app_context = app.app_context()
        self.app_context.push()
        database.create_all()

    def tearDown(self):
        database.session.remove()
        database.drop_all()
        self.app_context.pop()

    def test_produto_model(self):
        produto = Produto(nomeProduto='Teclado', categoriaProduto='Eletrônicos', estoque=10, valor=100)
        database.session.add(produto)
        database.session.commit()

        produto_saved = Produto.query.get(1)
        self.assertEqual(produto_saved.nomeProduto, 'Teclado')
        self.assertEqual(produto_saved.categoriaProduto, 'Eletrônicos')
        self.assertEqual(produto_saved.estoque, 10)
        self.assertEqual(produto_saved.valor, 100)

    def test_loginadm_model(self):
        loginadm = Loginadm(login='admin', senha='senha')
        database.session.add(loginadm)
        database.session.commit()

        loginadm_saved = Loginadm.query.get(1)
        self.assertEqual(loginadm_saved.login, 'admin')
        self.assertEqual(loginadm_saved.senha, 'senha')

if __name__ == '__main__':
    unittest.main()
