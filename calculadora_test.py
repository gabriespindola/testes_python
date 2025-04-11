import unittest
from calculadora import somar, dividir

class TestCalculador(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(1, 1), 1)
        with self.assertRaises(ValueError):
            dividir(1, 0)
if __name__ == '__main__':
    unittest.main()
