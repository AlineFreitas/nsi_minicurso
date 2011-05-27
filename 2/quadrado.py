#coding: utf-8
# 2) Crie uma classe que modele um quadrado e permita definir, alterar e consultar o tamanho dos lados e obter a área.
class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def obter_lado(self):
        return self.lado

    def alterar_lado(self, novo_lado):
        self.lado = novo_lado

    def area(self):
        return self.lado**2
