"""
Testes do Exercício 3.2 - Parâmetros e cifra RSA
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import unittest
from mod1_ex3_2 import *

class TestSum(unittest.TestCase):

    def test_gcd(self):   # Teste da função gcd
        self.assertEqual(gcd(9, 6), 3, "Devia ser 3")

    """
    Testes da função keys_rsa
    """
    def test_rsa(self):
        self.assertEqual(keys_rsa(5,11), ((55, 3), (55, 27)), "Devia ser ((55, 3), (55, 27))")

    def test_rsa(self):
        self.assertEqual(keys_rsa(23,13), ((299, 5), (299, 53)), "Devia ser ((299, 5), (299, 53))")
    

if __name__ == '__main__':
    unittest.main()




    