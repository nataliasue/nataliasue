class Cliente:
    def __init__(self, nome, email, senha, endereco):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.endereco = endereco
        
    @property
    def senha(self):
        return self.__senha