#coding: utf-8
import unittest
from should_dsl import should
from quadrado import Quadrado

class TestQuadrado(unittest.TestCase):

    def test_quadrado(self):
        quadrado = Quadrado(14)
        quadrado.obter_lado() |should| equal_to(14)

    def test_obter_lado(self):
        quadrado = Quadrado(7)
        quadrado.obter_lado() |should| equal_to(7)

    def test_alterar_lado(self):
        quadrado = Quadrado(10)
        quadrado.alterar_lado(8)
        quadrado.obter_lado() |should| equal_to(8)

    def test_calcular_area(self):
        quadrado = Quadrado(14)
        quadrado.area() |should| equal_to(196)

if __name__ == "__main__":
    unittest.main()
