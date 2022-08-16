n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = (n1 + n2 + n3) / 3
print(f'A média do aluno é: {media}')

if media > 7:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado por média.')