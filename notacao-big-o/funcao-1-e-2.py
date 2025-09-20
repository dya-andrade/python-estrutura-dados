# O(n)
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma # 10 vezes soma1(10) - 11 passos

import tempo

tempo.em_segundos(soma1, 10)

# O(3)
def soma2(n):
    return (n * (n + 1)) / 2 # soma2(10) - 3 passos

tempo.em_segundos(soma2, 10)

#import timeit as tm

#tempo = tm.timeit("soma1(10)", globals=globals(), number=10000)
#print(f"Tempo total: {tempo}")
#print(f"Tempo médio: {tempo/10000}")