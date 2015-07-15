#coding: utf-8
#2) Crie uma classe que modele um quadrado e permita definir, alterar e consultar o tamanho dos lados e obter a área.
class Quadrado
	attr_accessor :lado

	def initialize(lado)
		@lado = lado
	end
	
	def area
		@lado*@lado
	end
end