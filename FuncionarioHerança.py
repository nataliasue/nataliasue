class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        
    def salarioLiquido(self, itens_descontos):
        liquido = self._salario
        for desconto in itens_descontos:
            liquido -= desconto
            return liquido
        
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qt_gerenciados):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__qt_gerenciados = qt_gerenciados
        
gerente = Gerente('Ana', '12345678', 50000, '987654321', 10)
plano_saude = 300
inss = 200
i_r = 500
lista_descontos = [plano_saude, inss, i_r]
salario_liquido = gerente.salarioLiquido(lista_descontos)
print(salario_liquido)
        
    