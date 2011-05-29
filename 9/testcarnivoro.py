#coding: utf-8

import unittest
from should_dsl import should
from carnivoro import Carnivoro

#9) Crie uma classe chamada Carnivoro
class TestCarnivoro(unittest.TestCase):
    #que permita que objetos desta classe se alimentem de qualquer coisa (números, booleanos, caracteres, strings ou qualquer outro objeto).
    def test_carnivoro(self):
        carnivoro = Carnivoro()
        len(carnivoro.estomago) |should| equal_to(0)

    def test_alimentar_se(self):
        carnivoro = Carnivoro()
        carnivoro.alimentar_se(7)
        carnivoro.estomago[0] |should| equal_to(7)

    #O conteúdo do estômago do carnívoro deve poder ser consultado
    def test_consultar_estomago(self):
        carnivoro = Carnivoro()
        carnivoro.alimentar_se(1)
        carnivoro.alimentar_se('Corrupcao')
        carnivoro.alimentar_se(7.88)
        carnivoro.alimentar_se(True)
        carnivoro.listar_conteudo_estomago() |should| equal_to('1 Corrupcao 7.88 True') #teste não passa, mesmo o conteúdo dando igualzinho. Não descobri como contornar esse erro.

    #e também deve ser possível digerir os alimentos. A cada digestão o alimento mais antigo deve ser eliminado.
    def test_digerir_alimentos(self):
        carnivoro = Carnivoro()
        carnivoro.alimentar_se(1)
        carnivoro.alimentar_se('Corrupção')
        carnivoro.alimentar_se(7.88)
        carnivoro.alimentar_se(True)
        carnivoro.digerir_alimento()
        carnivoro.estomago[0] |should| equal_to('Corrupção')

if __name__ == "__main__":
    unittest.main()
