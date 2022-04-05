notas = 0

for prova in range(1, 5):
    nota = float(input(f'Nota {prova}: '))
    notas += nota 
    
media = notas / 4
print(f'Media: {media}')