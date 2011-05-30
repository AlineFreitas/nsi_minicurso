#coding: utf-8
# 12) Crie um objeto número que seja capaz de informar:
# a) se é par;
# b) se é ímpar;
# c) seu valor como número romano;
# d) o termo na série de fibonacci equivalente ao seu valor (por exemplo, o número 4 deve devolver o valor do 4º termo da série);
# e) seu fatorial (implementado em 3 formas: (1) com loop; (2) recursiva; (3) funcional (usando map, reduce etc)).
class Numero(int):

    def __init__(self, value):
        self.value = value

    # a) se é par ou b) se é ímpar;
    def par_ou_impar(self):
        valor = str(self.value)
        if int(valor[len(valor)-1])%2 == 0:
            return 'Par'
        else:
            return 'Impar'
    # c) seu valor como número romano;
    def converter_numeros_romanos(self):
        pass
    
    # d) o termo na série de fibonacci equivalente ao seu valor (por exemplo, o número 4 deve devolver o valor do 4º termo da série);
    def serie_fibonacci(self):
        anterior, atual = 0, 1
        for i in xrange(0,self.value)
            anterior, atual = atual, atual+anterior
        return atual
    
    # e) seu fatorial (implementado em 3 formas)

    #(1) com loop;
    def fatorial_loop(self):
        pass

    #(2) recursiva;
    def fatorial_recursivo(self):
        pass

    #(3) funcional (usando map, reduce etc)).
    def fatorial_funcional(self):
        pass
