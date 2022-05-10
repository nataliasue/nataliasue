import email
from Endereço import Endereço
from Cliente import  Cliente

nome = input('Digite aqui seu nome: ')
email = input('Digite aqui seu email: ')
senha = input('Digite aqui sua senha: ')

cep = int(input('Digite aqui seu cep: '))
rua = input('Digite aqui sua rua: ')
numero = int(input('Digite aqui o numero da casa: '))
cidade = input('Digite sua cidade: ')
estado = input('Digite seu estado: ')
pais = input('Digite seu país: ')

endereco1 = Endereço(cep, rua, numero, cidade, estado, pais)

cliente1 = Cliente(nome, email, senha, endereco1)
print('Nome: ', cliente1.nome)
print('Email: ', cliente1.email)
print('Endereço: ', cliente1.endereco.rua, ',', cliente1.endereco.numero)

