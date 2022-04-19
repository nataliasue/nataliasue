def retorna_somatorio(v):
    somatorio = 0

for i in range(1, v + 1):
    somatorio += i 
return somatorio

valor = int(input('Digite aqui um valor inteiro: '))
print(retorna_somatorio(valor))

