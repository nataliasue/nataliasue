class Funcionario:
    '''Dados do Funcionário'''
    def __init__ (self, nome, salario, matricula, funcao):
        self.nome = nome
        self.salario = salario
        self.matricula = matricula
        self.funcao = funcao
    
    @property
    def salario(self):
        return self.salario
    
    @salario.setter
    def salario(self, salario):
        salario = self.salario * 0.15
   