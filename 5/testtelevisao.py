#coding: utf-8
import unittest
from should_dsl import should
from televisao import Televisao

class TestTelevisao(unittest.TestCase):

    # Crie uma classe que modele uma televisão
    def test_televisao(self):
        televisao = Televisao()
        televisao.power |should| be(False)
        televisao.volume_maximo |should| equal_to(100)
        televisao.canal_maximo |should| equal_to(100)
        televisao.canal_atual |should| equal_to(3)
        televisao.catalogo_de_canais.items() |should| equal_to([(3, 'Default Satelite TV Channel'), ('AV', 'Audio/Video Channel')])
    
    #e que permita ligar e desligar a TV,
    def test_ligar(self):
        televisao = Televisao()
        televisao.ligar()
        televisao.power |should| be(True)

    def test_desligar(self):
        televisao = Televisao()
        televisao.ligar()
        televisao.desligar()
        televisao.power |should| be(False)

    #e alterar e consultar o número do canal e o volume.
    def test_alterar_canal(self):
        televisao = Televisao()
        televisao.alterar_canal('Default Satelite TV Channel', 4)
        televisao.catalogo_de_canais.items() |should| equal_to([(4, 'Default Satelite TV Channel'), ('AV', 'Audio/Video Channel')])
    
    #O número do canal e o volume somente podem ser alterados dentro de uma faixa válida.

if __name__ == "__main__":
    unittest.main()
