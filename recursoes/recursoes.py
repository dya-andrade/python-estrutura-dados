for _ in range(6):
    print('Recursão')

def recursao(i):
    print('Recursão')
    i += 1
    if i == 5:
        return # chegando aqui ele desempilha as chamadas
    else:
        recursao(i) # empilha as chamadas

print()

recursao(0)

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += 1
    return soma

def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1) 

print()

import tempo

tempo.em_segundos(soma1, 100)
tempo.em_segundos(soma2, 100) # mais custoso por empilhar e desempilhar

