"""
Testes do Exercício 1.4 - A cifra de Belaso-Vigènere
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import unittest
from mod1_ex1_4 import *

class TestSum(unittest.TestCase):

    def test_conversao_letra_numero(self):  # teste da função letra_para_numero
        self.assertEqual(letra_para_numero("a"), 0, "Devia ser 0")

    def test_conversao_numero_letra(self):  # teste da função numero_para_letra
        self.assertEqual(numero_para_letra(0), "A", "Devia ser A")

    """
    Testes da função belaso_vigenere
    """
    def test_bellaso_vigenere(self):
        self.assertEqual(belaso_vigenere("acifradebellaso", "BELLASO"), "BGTQRSRFFPWLSGP", "Devia ser BGTQRSRFFPWLSGP")

    def test_bellaso_vigenere2(self):
        self.assertEqual(belaso_vigenere("primeiracifrapolialfabeticacomtrocadechave", "ZAR"), "ORZLEZQATHFIZPFKIRKFRAEKHCRBODSRFBAUDCYZVV", "Devia ser ORZLEZQATHFIZPFKIRKFRAEKHCRBODSRFBAUDCYZVV")

if __name__ == '__main__':
    unittest.main()




    