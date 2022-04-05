salario = float(input('Salario: '))
valor_prestação = float(input('Valor da prestação: '))

if valor_prestação > (salario * 0.20):
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido') 