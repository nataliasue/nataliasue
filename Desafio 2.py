cliente = []
clientes = {}

while True:    
    cliente = []
    cliente['Nome'] = str(input('Nome do cliente: '))
    cliente['Telefone'] = int(input('Telefone do cliente: '))
    cliente['Email'] = str(input('Email do cliente: '))
    print(cliente)
    
    proximo = str(input('Próximo cliente?: [S/N] '))
    if proximo == 'S':
        print('Próximo cliente.')
    elif proximo == 'N':
        print('Você saiu do sistema.')
        break
       
    clientes.append(cliente)
        
   
    
    

    
    
    