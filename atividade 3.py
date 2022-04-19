def ordem_crescente(a, b, c):
    if a < b and a < c and b < c:
        return a, b, c 
    elif b < a and b < c and a c < a:
        return b, c, a 
    elif b < a and c < b and a < b:
        return 

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

ordenados = ordem_crescente(num1, num2, num3)