import unittest
from verificaPar import verifica

class VerificaPar(unittest.TestCase):
    def test_verificaPar(self):
        self.assertTrue(verifica(2))
        self.assertTrue(verifica(4))
        self.assertFalse(verifica(3))
        self.assertTrue(verifica(-4))

if __name__ == '__main__':
    unittest.main()