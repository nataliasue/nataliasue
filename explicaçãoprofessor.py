from random import randrange 
numeroSorteado = randrange(1, 10)
print(numeroSorteado)


while True:
    palpite = int(input('Digite aqui seu palpite: '))
    
    if palpite == numeroSorteado:
        print('Parabéns, você acertou!')
        break
    elif palpite > numeroSorteado:
        print('Digite um número menor.')
    elif palpite < numeroSorteado:
        print('Digite um número maior.')