# 9) Crie uma classe chamada Carnivoro que permita que objetos desta classe se alimentem de qualquer coisa (números, booleanos, caracteres, strings ou qualquer outro objeto). O conteúdo do estômago do carnívoro deve poder ser consultado e também deve ser possível digerir os alimentos. A cada digestão o alimento mais antigo deve ser eliminado.
#coding: utf-8
class Carnivoro
    attr_accessor :estomago
 
    def initialize
        @estomago = []
    end
    
    def alimentar_se(algo)
        @estomago.push(algo)
    end

    def digerir
        @estomago.shift
    end
end