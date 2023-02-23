"""
Exercício 4.1 - Construção de Merkle-Damgård
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import unittest
from mod1_ex4_1 import *

class TestSum(unittest.TestCase):

    def test_splitToBlocks(self):   # Teste da função splitToBlocks
        self.assertEqual(splitToBlocks('010101010101010000'), ['010101010101', '010000100000', '000000001100'], "Devia ser ['010101010101', '010000100000', '000000001100']")

    def test_oneZerosPadding(self):   # Teste da função oneZerosPadding
        self.assertEqual(oneZerosPadding('010101010', 12), '010101010100', "Devia ser '010101010100'")

    def test_fillLengthBlock(self):   # Teste da função fillLengthBlock
        self.assertEqual(fillLengthBlock(12), '000000001100', "Devia ser '000000001100'")  

    def test_hashProcess(self):   # Teste da função hashProcess
        self.assertEqual(hashProcess('010101010100', '1111'), '1101', "Devia ser '1101'")  

    """
    Teste da função hash_MD_funcaof
    """
    def test_hash(self):   
        self.assertEqual(hash_MD_funcaof('010101010101010000', '1111'), ['1111', '1110', '0100', '0000'], "Devia ser ['1111', '1110', '0100', '0000']")  
    

if __name__ == '__main__':
    unittest.main()





