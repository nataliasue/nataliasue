listaClientes = []
dadosCliente = {}

clienteNome = str(input('Nome do cliente: '))
telefoneCliente = int(input('Telefone do cliente: '))
emailCliente = str(input('Email do cliente: '))

listaClientes = [{'Nome do cliente':clienteNome, 
'Telefone do cliente':telefoneCliente,
'Email do cliente':emailCliente}]

dadosCliente['Nome'] = input('Nome do cliente: ')
dadosCliente['Telefone'] = input('Telefone do cliente: ')
dadosCliente['Email'] = input('Email do cliente: ')

listaClientes.append(dadosCliente)
print(listaClientes)
