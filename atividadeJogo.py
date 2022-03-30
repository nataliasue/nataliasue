from random import randrange 
numeroSorteado = randrange(1, 10)
print(numeroSorteado)

palpiteUsuário = int(input('Digite seu palpite: '))
    
if palpiteUsuário < numeroSorteado:
    print('Este número é menor que o número sorteado, tente novamente.')
elif palpiteUsuário > numeroSorteado:
    print('Este valor é maior que o número sorteado, tente novamente.')
elif palpiteUsuário == numeroSorteado:
    print('Parabéns, você acertou o número sorteado!')