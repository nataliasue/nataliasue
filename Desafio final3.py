clientes = list()
cliente = dict()

while True:
    cliente.clear()
    cliente['Nome'] = str(input('Nome do cliente: '))
    cliente['Telefone'] = int(input('Telefone do cliente: '))
    cliente['Email'] = str(input('Email do cliente: '))
    print(cliente)
    break

while True:
    proximo = str(input('Próximo cliente?: [S/N] ')).upper()[0]
    if proximo == 'S':
        print('Próximo cliente.')
    cliente['Nome'] = str(input('Nome do cliente: '))
    cliente['Telefone'] = int(input('Telefone do cliente: '))
    cliente['Email'] = str(input('Email do cliente: '))
    print(cliente)
    
    if proximo == 'N':
        break

clientes.append(cliente.copy())
