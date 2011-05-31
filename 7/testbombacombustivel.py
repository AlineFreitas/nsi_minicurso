#coding: utf-8
import unittest
from should_dsl import should
from bombacombustivel import Bomba

# 7) Crie uma classe que modele uma bomba de combustível
class TestBomba(unittest.TestCase):

    #e permita definir a capacidade da bomba, o preço do combustível por litro
    def test_bomba(self):
        bomba = Bomba(5000, 1.689)
        bomba.capacidade_maxima |should| equal_to(5000)
        bomba.preco_litro |should| equal_to(1.689)
        bomba.capacidade_atual |should| equal_to(0)

    #permita encher a bomba (sempre encher completamente) e consultar sua quantidade de combustível.
    def test_encher_bomba(self):
        bomba = Bomba(5000, 1.689)
        bomba.encher_bomba()
        bomba.capacidade_atual |should| equal_to(5000)

    def test_consultar_reserva(self):
        bomba = Bomba(5000, 1.689)
        bomba.consultar_reserva() |should| equal_to(0)
        bomba.encher_bomba()
        bomba.consultar_reserva() |should| equal_to(5000)

    #seja permitido abastecer por valor (retornando a quantidade de combustível abastecida)
    def test_abaster_por_preco(self):
        bomba = Bomba(5000, 1.689)
        bomba.encher_bomba()
        bomba.abastecer_valor(16.89) |should| equal_to(10)

    #abastecer por quantidade de litros (retornando o valor a ser pago).
    def test_abaster_por_litro(self):
        bomba = Bomba(5000, 1.689)
        bomba.encher_bomba()
        bomba.abastecer_litro(10) |should| equal_to(16.89)

    #Deve ser permitido também alterar o valor do preço por litro.
    def test_alterar_preco_do_litro(self):
        bomba = Bomba(5000, 1.689)
        bomba.alterar_preco_litro(2.95)
        bomba.preco_litro |should| equal_to(2.95)

    #Deve ser tratada a situação de não haver combustível suficiente na bomba para um determinado abastecimento.
    def test_abastecer_litro_alem_reserva(self):
        bomba = Bomba(5000, 1.689)
        bomba.capacidade_atual |should| equal_to(0)
        bomba.abastecer_litro(10) |should| equal_to('Reserva Insuficiente. Operação Abortada')

    def test_abastecer_preco_alem_reserva(self):
        bomba = Bomba(5000, 1.689)
        bomba.abastecer_valor(16.89) |should| equal_to('Reserva Insuficiente. Operação Abortada')

if __name__ == "__main__":
    unittest.main()
