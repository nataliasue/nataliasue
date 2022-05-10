class Carro:
    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca 
        self.ano = ano 
        self.__preco = preco
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor == 0:
            return self.__preco
        elif valor <= 50000:
            return self.__preco
        self.__preco = valor
        return self.__preco
        
        
        
        
        
    
        
   
    
    

    
    
    