peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso/altura*2)
print(f'Seu IMC é de: {imc}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no seu peso normal.')
elif imc < 30:
    print('Você está no sobrepeso')
elif imc > 30:
    print('Você está na obesidade.')