#coding: utf-8
#8) Crie uma classe que modele um retângulo e permita definir a altura e a base. A classe tambem deve permitir definir e alterar o ponto que representa o centro do retângulo e permitir que sejam consultados os pontos dos quatro vértices. Um ponto deve ser modelado por outra classe, e deve permitir definir e consultar valores x e y do ponto. Após o centro ser alterado, novas consultas aos vértices devem retornar os valores atualizados. O objeto também deve informar sua área, seu perímetro e se é um quadrado.

require_relative 'ponto'

class Retangulo
	attr_accessor :altura, :base, :ponto_central, :vertice_a, :vertice_b, :vertice_c, :vertice_d

	def initialize(altura, base)
		@altura = altura
		@base = base
		@ponto_central = Ponto.new(base/2.0, altura/2.0)

		#Seguindo 
        @vertice_a = Ponto.new(0, 0)
		@vertice_b = Ponto.new(0, altura)
		@vertice_c = Ponto.new(base, altura)
		@vertice_d = Ponto.new(base, 0)
	end

	def ponto_central=(novo_ponto)
		if novo_ponto.class == Ponto
			@vertice_a = Ponto.new(novo_ponto.x - (@base/2.0), novo_ponto.y - (@altura/2.0))
            @vertice_b = Ponto.new(novo_ponto.x - (@base/2.0), novo_ponto.y + (@altura/2.0))
            @vertice_c = Ponto.new(novo_ponto.x + (@base/2.0), novo_ponto.y + (@altura/2.0))
            @vertice_d = Ponto.new(novo_ponto.x + (@base/2.0), novo_ponto.y - (@altura/2.0))
		else
			return 'Error, not a instance of the Ponto class'
		end
	end

    def perimetro
        return 2 * @base + 2 * @altura
    end

    def area
        return @base * @altura
    end

    def quadrado?
        if @base == @altura
            return true
        else
            return false
        end
    end
end