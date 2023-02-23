"""
Testes do Exercício 2.2 - Comparação de cifras de substituição em bytes
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import unittest
from mod1_ex2_2 import *

class TestSum(unittest.TestCase):

    def test_split_sequence(self):  # Teste da função split_sequence
        self.assertEqual(split_sequence("1010",2), ['10','10'], "Devia ser [10,10]")

    """
    Testes da função cifras_sustituicao_bytes para os vários valores de n (1,2,4,8)
    """
    def test_n1(self):
        self.assertEqual(cifras_sustituicao_bytes("11111110", 1), "00101011", "Devia ser 00101011")

    def test_n2(self):
        self.assertEqual(cifras_sustituicao_bytes("11111110", 2), "10000011", "Devia ser 10000011")

    def test_n4(self):
        self.assertEqual(cifras_sustituicao_bytes("11111110", 4), "11000011", "Devia ser 11000011")

    def test_n8(self):
        self.assertEqual(cifras_sustituicao_bytes("11111110", 8), "11010011", "Devia ser 11010011")

    

if __name__ == '__main__':
    unittest.main()




    