numero = int(input('Digite um número: '))
print(numero)

if numero % 2 == 0:
    print('Este número é par')
elif numero % 2 == 1:
    print('Este número é impar')
elif numero == 0:
    print('Este número é 0')
    
#Posso colocar o Else no ultimo Elif