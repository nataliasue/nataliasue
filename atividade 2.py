nome_usuario = input('Nome: ')
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = int(input('Ano atual: '))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print(f'{nome_usuario}, sua entrada foi permitida')
else:
    print(f'{nome_usuario}, sua entrada não foi permitida')