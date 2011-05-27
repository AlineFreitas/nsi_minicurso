#coding: utf-8
import unittest
from should_dsl import should
from bola import Bola

class TestBola(unittest.TestCase):

    def test_definir_cor(self):
        bola = Bola()
        bola.definir_cor('Azul')
        bola.obter_cor() |should| equal_to ('Azul')

    def test_obter_cor(self):
        bola = Bola()
        bola.definir_cor('Azul')
        bola.obter_cor() |should| equal_to('Azul')

    def test_alterar_cor(self):
        bola = Bola()
        bola.definir_cor('Azul')
        bola.alterar_cor('Preta')
        bola.obter_cor() |should| equal_to('Preta')

if __name__ == "__main__":
    unittest.main()
