#coding: utf-8
# 7) Crie uma classe que modele uma bomba de combustível e permita definir a capacidade da bomba, o preço do combustível por litro e permita encher a bomba (sempre encher completamente) e consultar sua quantidade de combustível. É necessário também que seja permitido abastecer por valor (retornando a quantidade de combustível abastecida), abastecer por quantidade de litros (retornando o valor a ser pago). Deve ser permitido também alterar o valor do preço por litro. Deve ser tratada a situação de não haver combustível suficiente na bomba para um determinado abastecimento.

class Bomba(object):

    def __init__(self, capacidade_maxima, preco_litro):
        self.capacidade_maxima = capacidade_maxima
        self.preco_litro = preco_litro
        self.capacidade_atual = 0

    def encher_bomba(self):
        self.capacidade_atual = self.capacidade_maxima

    def consultar_reserva(self):
        return self.capacidade_atual

    def abastecer_valor(self, dinheiro_recebido):
        if (dinheiro_recebido/self.preco_litro) <= self.capacidade_atual:
            self.capacidade_atual-= dinheiro_recebido/self.preco_litro
            return dinheiro_recebido/self.preco_litro
        else:
            return 'Reserva Insuficiente. Operação Abortada'

    def abastecer_litro(self, litros_desejados):
        if self.capacidade_atual >= litros_desejados:
            self.capacidade_atual-=litros_desejados
            return self.preco_litro*litros_desejados
        else:
            return 'Reserva Insuficiente. Operação Abortada'

    def alterar_preco_litro(self, novo_preco_litro):
        self.preco_litro = novo_preco_litro
