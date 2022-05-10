class Endereço:
    def __init__(self, cep, rua, numero, cidade, estado, pais, complemento =None):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.estado = estado
        self.pais = pais
        self.complemento = complemento
        
        