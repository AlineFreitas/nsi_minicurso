#coding: utf-8
# 4) Crie uma classe que modele uma pessoa e permita definir e obter a idade, peso e altura da pessoa e que permita fazer a pessoa envelhecer, engordar e emagrecer. A cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 1,5 cm.
class Pessoa(object):

    def __init__(self, idade, peso, altura):
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return float(self.altura)

    def obter_peso(self):
        return float(self.peso)

    def envelhecer(self):
        if self.idade < 21:
            self.altura+=float(0.015)
        self.idade+=1

    def engordar(self, peso_ganho):
        self.peso+=float(peso_ganho)

    def emagrecer(self, peso_eliminado):
        self.peso-=float(peso_eliminado)
