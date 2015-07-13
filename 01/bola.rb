#coding: utf-8
#1) Crie uma classe que modele uma bola e permita trocar e consultar a cor da bola.
class Bola
	attr_accessor :color

	def initialize(color)
		@color= color
	end
end