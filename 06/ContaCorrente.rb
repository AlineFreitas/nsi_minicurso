#coding:utf-8
#6) Crie uma classe que modele uma conta corrente e que permita definir e consultar o numero da conta e o nome correntista, consultar o saldo e fazer depósitos e saques.
class ContaCorrente
	attr_accessor

	def initialize(nome_titular, numero_conta, saldo_inicial=0)
		@nome_titular = nome_titular
		@numero_conta = numero_conta
		@saldo_atual = saldo_inicial
	end
	
	def depositar(valor)
		@saldo+= valor
	end

	def saque(valor)
		if valor <= @saldo
			@saldo-= valor
		else
			puts 'Saldo Insuficiente!'
		end
	end
end