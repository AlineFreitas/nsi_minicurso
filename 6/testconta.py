#coding: utf-8
import unittest
from should_dsl import should
from conta import Conta

# 6) Crie uma classe que modele uma conta corrente
class TestConta(unittest.TestCase):
    #e que permita definir e consultar o numero da conta e o nome correntista
    def test_conta(self):
        conta = Conta('Ricks Rox', 200.00)
        conta.saldo |should| equal_to(200.0)
        conta.numero_conta |should| equal_to(2)
        conta.titular_correntista |should| equal_to('Ricks Rox')

    #consultar o saldo e fazer depósitos e saques.
    def test_consultar_saldo(self):
        conta = Conta('Ricks Rox', 200.00)
        conta.numero_conta |should| equal_to(1)
        conta.consultar_saldo() |should| equal_to(200.00)

    def test_efetuar_saque(self):
        conta = Conta('Ricks Rox', 500.00)
        conta.saque(300.00)
        conta.consultar_saldo() |should| equal_to(200.00)

    def test_efetuar_saque_negativo(self):
        conta = Conta('Ricks Rox', 500.00)
        conta.saque(-200.00) |should| equal_to("Valor inválido!")

    def test_efetuar_saque_excessivo(self):
        conta = Conta('Ricks Rox', 500.00)
        conta.saque(600.00) |should| equal_to('Saldo insuficiente. Operação Abortada!')

    def test_efetuar_deposito(self):
        conta = Conta('Ricks Rox')
        conta.deposito(200)
        conta.consultar_saldo() |should| equal_to(200.00)

    def test_efetuar_deposito_negativo(self):
        conta = Conta('Ricks Rox')
        conta.deposito(-100) |should| equal_to("Valor inválido. Operação Abortada!")
        conta.consultar_saldo() |should| equal_to(0.00)

if __name__ == "__main__":
    unittest.main()
