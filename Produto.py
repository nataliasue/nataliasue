class Produto:
    '''Modelo do produto'''
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.__preco = valor
        self.descrição = descricao 
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novopreco):
        if novopreco > 0:
            self.__preco = novopreco
        

p1 = Produto('Boné', 80, 'Boné Preto')
p1.preco = 70
print(p1.preco)
