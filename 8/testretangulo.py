#coding: utf-8

import unittest
from should_dsl import should
from retangulo import Retangulo

# 8) Crie uma classe que modele um retângulo
class TestRetangulo(unittest.TestCase):

    #e permita definir a altura e a largura.
    def test_retangulo(self):
        pass

    # A classe tambem deve permitir definir e alterar o ponto que representa o centro do retângulo
    def test_definir_ponto_central(self):
        pass

    #e permitir que sejam consultados os pontos dos quatro vértices. 
    def test_consultar_pontos_do_vertice(self):
        pass

    #Após o centro ser alterado, novas consultas aos vértices devem retornar os valores atualizados.
    def test_retorna_valores_atualizados(self):
        pass

    #O objeto também deve informar sua área, seu perímetro e se é um quadrado.
    def test_area(self):
        pass
    def test_perimetro(self):
        pass
    def test_sou_quadrado(self)
        pass

if __name__ == "__main__":
    unittest.main()
