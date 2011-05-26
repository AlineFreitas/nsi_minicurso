#coding: utf-8
# 1) Crie uma classe que modele uma bola e permita trocar e consultar a cor da bola.
class Bola(object):
    
    def obter_cor(self):
        return self.cor

    def definir_cor(self, cor):
        self.cor = cor

    def alterar_cor(self, nova_cor):
        self.cor = nova_cor
