#coding: utf-8
# 6) Crie uma classe que modele uma conta corrente e que permita definir e consultar o numero da conta e o nome correntista, consultar o saldo e fazer depósitos e saques.
class Conta(object):
    numero_conta = 0
    def __init__(self, titular_correntista, saldo=0):
        self.numero_conta = Conta.numero_conta+1
        self.titular_correntista = titular_correntista
        self.saldo = float(saldo)
        Conta.numero_conta+=1

    def consultar_saldo(self):
        return self.saldo

    def saque(self, valor_retirado):
        if self.saldo < valor_retirado:
            return "Saldo insuficiente. Operação Abortada!"
        elif self.saldo >= valor_retirado > 0:
            self.saldo-=float(valor_retirado)
        else:
            return "Valor inválido!"

    def deposito(self, valor_depositado):
       if valor_depositado <=0:
           return "Valor inválido. Operação Abortada!"
       else:
           self.saldo+=valor_depositado
