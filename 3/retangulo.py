#coding: utf-8
# 3) Crie uma classe que modele um retângulo e permita definir, alterar e consultar os valores dos lados, obter a área e obter o perímetro.
class Retangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def alterar_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def consultar_lados(self):
        return (self.base, self.altura)

    def obter_perimetro(self):
        return self.base*2 + self.altura*2

    def obter_area(self):
        return self.base * self.altura

    def __repr__(self):
        return 'Retangulo(%i, %i)' %(self.base, self.altura)
