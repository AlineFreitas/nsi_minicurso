#coding: utf-8
import unittest
from should_dsl import should
from retangulo import Retangulo

class TestRetangulo(unittest.TestCase):

    def test_retangulo(self):
        retangulo = Retangulo(5, 4)
        retangulo.base |should| equal_to(5)
        retangulo.altura |should| equal_to(4)

    def test_alterar_lados(self):
        retangulo = Retangulo(5, 4)
        retangulo.alterar_lados(8, 10)
        retangulo.__repr__() |should| equal_to('Retangulo(8, 10)')

    def test_consultar_lados(self):
        retangulo = Retangulo(5, 4)
        retangulo.consultar_lados() |should| equal_to((5, 4))

    def test_obter_perimetro(self):
        retangulo = Retangulo(5, 4)
        retangulo.obter_perimetro() |should| equal_to(18)

    def test_obter_area(self):
        retangulo = Retangulo(5, 4)
        retangulo.obter_area() |should| equal_to(20)

if __name__ == "__main__":
    unittest.main()
