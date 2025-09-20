# 0(1000) -> O(n)
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

import tempo

tempo.em_segundos(lista1)

# O(1) -> 1 passo
def lista2():
    return range(1000)

tempo.em_segundos(lista2)
