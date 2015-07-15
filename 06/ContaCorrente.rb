#coding:utf-8
#6) Crie uma classe que modele uma conta corrente e que permita definir e consultar o numero da conta e o nome correntista, consultar o saldo e fazer depósitos e saques.

class ContaCorrente
	attr_accessor :saldo
	attr_reader :nome_titular, :numero_conta

	def initialize(nome_titular, numero_conta, saldo=0)
		@nome_titular = nome_titular
		@numero_conta = numero_conta
		@saldo = saldo
	end
	
	def depositar(valor)
		@saldo+= valor
	end

	def saque(valor)
		if valor <= @saldo
			@saldo-= valor
		else
			puts 'Saldo Insuficiente! Não foi possível realizar essa operação.'
		end
	end
end