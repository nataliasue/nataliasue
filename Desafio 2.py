#Utlizei {} para colocar a variável clientes dentro de um dicionáio
#Em seguida tilizei [] para colocar a variável cliente em uma lista
clientes = {}
cliente = []

#Criei um laço para fazer o cadastro de cada novo cliente
while True:    
    cliente = []
#Fiz um input para saber os dados dos clientes
    cliente['Nome'] = str(input('Nome do cliente: '))
    cliente['Telefone'] = int(input('Telefone do cliente: '))
    cliente['Email'] = str(input('Email do cliente: '))
    print(cliente)

#Puxei uma nova variavel para saber se o somellier deseja cadastrar outro cliente ou não
    
    proximo = str(input('Próximo cliente?: [S/N] '))
    if proximo == 'S':
        print('Próximo cliente.')
    elif proximo == 'N':
        print('Você saiu do sistema.')
        break
#Utilização do break para parar caso o somellier termine o expediente e saia do sistema       
    clientes.append(cliente)
        
   
    
    

    
    
    