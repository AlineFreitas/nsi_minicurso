#coding: utf-8

import unittest
from should_dsl import should
from numero import Numero

class TestNumero(unittest.TestCase):
    
    # a) se é par ou b) se é ímpar;
    def test_par_ou_impar(self):
        numero = Numero(10)
        numero.par_ou_impar() |should| equal_to('Par')
        numero2 = Numero(11)
        numero2.par_ou_impar() |should| equal_to('Impar')
        numero3 = Numero(0)
        numero3.par_ou_impar() |should| equal_to('Par')

    # c) seu valor como número romano;
    def test_converter_numeros_romanos(self):
        pass
    
    # d) o termo na série de fibonacci equivalente ao seu valor (por exemplo, o número 4 deve devolver o valor do 4º termo da série);
    def test_serie_fibonacci(self):
        pass
    
    # e) seu fatorial (implementado em 3 formas)

    #(1) com loop;
    def test_fatorial_loop(self):
        pass

    #(2) recursiva;
    def test_fatorial_recursivo(self):
        pass

    #(3) funcional (usando map, reduce etc)).
    def test_fatorial_funcional(self):
        pass #Não sei implementar assim

if __name__ == "__main__":
    unittest.main()
