#coding: utf-8
# 3) Crie uma classe que modele um retângulo e permita definir, alterar e consultar os valores dos lados, obter a área e obter o perímetro.
class Retangulo
	attr_accessor :base, :altura

	def initialize(base, altura)
		@base = base
		@altura = altura
	end
	
	def area
		@base * @altura
	end

	def perimetro
		(2 * base) + (2 * altura)
	end
end