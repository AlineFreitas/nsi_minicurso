#coding: utf-8

#9) Crie uma classe chamada Carnivoro que permita que objetos desta classe se alimentem de qualquer coisa (números, booleanos, caracteres, strings ou qualquer outro objeto). O conteúdo do estômago do carnívoro deve poder ser consultado e também deve ser possível digerir os alimentos. A cada digestão o alimento mais antigo deve ser eliminado.
class Carnivoro(object):

    def __init__(self):
        self.estomago =[]

    def alimentar_se(self, alimento):
        self.estomago.append(alimento)

    def digerir_alimento(self):
        if len(self.estomago)>0:
            self.estomago.__delitem__(0)

    def listar_conteudo_estomago(self):
        lista_conteudo_estomago=''
        for alimento in self.estomago:
            lista_conteudo_estomago+=str(alimento)+' '
        return lista_conteudo_estomago
