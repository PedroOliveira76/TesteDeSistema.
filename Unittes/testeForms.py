import unittest
from MaxMercado.forms import FormLogin, FormCadProduto, FormEditProduto, FormSearchProd, FormDeletProduto
from MaxMercado import app

class TestForms(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_form_login(self):
        form = FormLogin(admin="admin123", senha="senha123")
        self.assertTrue(form.validate())

    def test_form_cad_produto(self):
        form = FormCadProduto(nomeProduto="Produto A", categoriaProduto="Categoria A", estoque=10, valor=100.0)
        self.assertTrue(form.validate())

    def test_form_edit_produto(self):
        form = FormEditProduto(idProduto=1, nomeProduto="Produto B", categoriaProduto="Categoria B", estoque=5, valor=50.0)
        self.assertTrue(form.validate())

    def test_form_search_prod(self):
        form = FormSearchProd(nomeProduto="Produto A")
        self.assertTrue(form.validate())

    def test_form_delet_produto(self):
        form = FormDeletProduto(id=1)
        self.assertTrue(form.validate())

if __name__ == '__main__':
    unittest.main()
