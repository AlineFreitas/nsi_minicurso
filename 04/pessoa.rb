#coding: utf-8
#4) Crie uma classe que modele uma pessoa e permita definir e obter a idade, peso e altura da pessoa e que permita fazer a pessoa envelhecer, engordar e emagrecer. A cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 1,5 cm.

class Pessoa
	attr_reader :nome, :idade, :peso, :altura

	def initialize(nome, idade, peso, altura)
		@nome = nome
		@idade = idade
		@peso = peso
		@altura = altura
	end

	def envelhecer
		@idade+= 1
		if @idade < 21
			@altura+= 0.015
		end
	end

	def engordar(ganho)
		@peso+= ganho
	end

	def emagrecer(perda)
		@peso-= perda
	end
end