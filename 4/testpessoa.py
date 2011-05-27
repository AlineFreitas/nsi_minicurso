#coding: utf-8
import unittest
from should_dsl import should
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def test_pessoa(self):
        pessoa = Pessoa(20, 78.5, 1.89)
        pessoa.obter_idade() |should| equal_to(20)
        pessoa.obter_peso() |should| equal_to(78.5)
        pessoa.obter_altura() |should| equal_to(1.89)

    def test_emagrecer(self):
        pessoa = Pessoa(20, 78.5, 1.89)
        pessoa.emagrecer(20.5)
        pessoa.obter_peso() |should| equal_to(58.0)

    def test_engordar(self):
        pessoa = Pessoa(20, 78.5, 1.89)
        pessoa.engordar(1.5)
        pessoa.obter_peso() |should| equal_to(80.0)

    def test_envelhecer(self):
        pessoa = Pessoa(21, 78.5, 1.89)
        pessoa.envelhecer()
        pessoa.obter_idade() |should| equal_to(22)

    def test_envelhecer_sem_crescer(self):
        pessoa = Pessoa(21, 78.5, 1.89)
        pessoa.obter_altura() |should| equal_to(1.89)

    def test_envelhecer_crescendo(self):
        pessoa = Pessoa(20, 78.5, 1.89)
        pessoa.envelhecer()
        pessoa.obter_idade() |should| equal_to(21)
        str(pessoa.obter_altura()) |should| equal_to('1.905') #problema de aproximação, corrigido usando string

if __name__ == "__main__":
    unittest.main()
