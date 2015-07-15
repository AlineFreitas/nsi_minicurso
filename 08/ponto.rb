# Um ponto deve ser modelado por outra classe, e deve permitir definir e consultar valores x e y do ponto.

class Ponto
	attr_accessor :x, :y

	def initialize(x, y)
		@x = x
		@y = y
	end

    def to_s
        return "P(#{@x}, #{@y})"
    end
end