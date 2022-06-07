class Cliente:
    def __init__(self, nome, cpf, email, senha, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha
        self.__endereco = endereco

@property
def nome(self):
    return self.__nome

@nome.setter
def nome (self, nome):
    self.nome = nome

@property
def cpf(self):
    return self.__cpf

@cpf.setter
def cpf (self, cpf):
    self.cpf = cpf

@property
def email(self):
    return self.__email

@email.setter
def email (self, email):
    self.email = email

@property
def senha(self):
    return self.__senha

@senha.setter
def senha (self, senha):
    self.senha = senha

@property
def endereco(self):
    return self.__endereco

@endereco.setter
def endereco (self, endereco):
    self.endereco = endereco