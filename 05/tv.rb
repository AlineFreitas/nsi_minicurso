#coding: utf-8
# 5) Crie uma classe que modele uma televisão e que permita ligar e desligar a TV, e alterar e consultar o número do canal e o volume. O número do canal e o volume somente podem ser alterados dentro de uma faixa válida.

#por padrão a tv é criada desligada, no volume 70 e no canal 3
#Faixa de volume de 0 a 100 e faixa de canais de 0 a 1000
class TV
	attr_accessor :channel
	attr_reader :on

	def initialize
		@on = false
		@min_volume, @max_volume = 0, 100
		@min_channel, @max_channel = 1, 1000
		@volume = 70
		@channel = 1
	end

	def up_volume
		@volume+= 1
	end

	def down_volume
		@volume-= 1
	end

	def up_channel
		if @channel < @max_channel
			@channel+= 1
		end
	end

	def down_channel
		if @channel > @min_channel
			@channel-= 1
		end
	end

	def turn_on
		@on = true
	end

	def turn_off
		@on = false
	end

	def channel=(new_channel)
		if (@min_channel..@max_channel).include?(new_channel)
			@channel = new_channel
		else
			puts 'Valor inválido!'
		end
	end
end