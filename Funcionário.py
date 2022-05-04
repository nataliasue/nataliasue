class Funcionario:
    '''Dados do Funcionário'''
    def __init__ (self, nome, salario, matricula, funcao):
        self.nome = nome
        self.__salario = salario
        self.matricula = matricula
        self.funcao = funcao
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, ajuste):
        if ajuste < self.__salario:
            return self.__salario
        elif ajuste <= self.__salario * 1.2:
            self.__salario = ajuste
            return self.__salario
   