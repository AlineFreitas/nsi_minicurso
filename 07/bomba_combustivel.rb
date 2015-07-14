#coding: utf-8
# 7) Crie uma classe que modele uma bomba de combustível e permita definir a capacidade da bomba, o preço do combustível por litro e permita encher a bomba (sempre encher completamente) e consultar sua quantidade de combustível. É necessário também que seja permitido abastecer por valor (retornando a quantidade de combustível abastecida), abastecer por quantidade de litros (retornando o valor a ser pago). Deve ser permitido também alterar o valor do preço por litro. Deve ser tratada a situação de não haver combustível suficiente na bomba para um determinado abastecimento.

class BombaCombustivel
	attr_reader :capacidade_total
	attr_accessor :capacidade_atual, :preco_por_litro

	def initialize(capacidade_em_litros=0)
		@capacidade_total = capacidade_em_litros
		@capacidade_atual = nil
		@preco_por_litro = nil
	end
	
	def encher_bomba
		@capacidade_atual = @capacidade_total
	end

	def abastecer_por_valor(valor)
		litros = valor/preco_por_litro
		if litros <= @capacidade_atual
			@capacidade_atual-= litros
			return litros
		else
			puts 'A bomba não tem combustível suficiente para realizar esse abastecimento'
		end
	end

	def abastecer_por_litro(litros)
		if litros <= @capacidade_atual
			valor = litros * @preco_por_litro
			@capacidade_atual-= litros
			return valor
		else
			puts 'A bomba não tem combustível suficiente para realizar esse abastecimento'
		end
	end
end