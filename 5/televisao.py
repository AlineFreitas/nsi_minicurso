#coding: utf-8
# 5) Crie uma classe que modele uma televisão e que permita ligar e desligar a TV, e alterar e consultar o número do canal e o volume. O número do canal e o volume somente podem ser alterados dentro de uma faixa válida.
class Televisao(object):

    def __init__(self):
        self.power = False
        self.catalogo_de_canais = {3:'Default Satelite TV Channel', 'AV':'Audio/Video Channel'}
        self.volume_maximo = 100
        self.canal_maximo = 100
        self.canal_atual = 3

    def ligar(self):
        self.power = True

    def desligar(self):
        self.power = False

    def alterar_canal(self, descricao_canal_a_ser_alterado, novo_numero):
        
