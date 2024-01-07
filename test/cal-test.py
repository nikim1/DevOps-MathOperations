import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        result = self.app.get('/add/5/3')
        self.assertEqual(result.data.decode('utf-8'), '8')

    def test_subtract(self):
        result = self.app.get('/subtract/10/3')
        self.assertEqual(result.data.decode('utf-8'), '7')

    def test_multiply(self):
        result = self.app.get('/multiply/5/4')
        self.assertEqual(result.data.decode('utf-8'), '20')

    def test_divide(self):
        result = self.app.get('/divide/15/3')
        self.assertEqual(result.data.decode('utf-8'), '5')

    def test_divide_by_zero(self):
        result = self.app.get('/divide/5/0')
        self.assertEqual(result.status_code, 500)


if __name__ == '__main__':
    unittest.main()
