def selection_sort(vetor):
    n = len(vetor) # 4

    for i in range(n): # 4 - 1 = 3, pois começa com 0
        indice_menor = i
        comeco_ordenada = i + 1 # 0 + 1 = 1
        for j in range(comeco_ordenada, n): # 1 até 4
            # esquerda > direita
            if vetor[indice_menor] > vetor[j]:
                indice_menor = j
        # 3 passos
        temp = vetor[i]
        vetor[i] = vetor[indice_menor]
        vetor[indice_menor] = temp

    return vetor

def selection_sort2(lista):
    n = len(lista)

    # Percorre cada posição do vetor (exceto a última)
    for i in range(n - 1):
        indice_menor = i

        # Encontra o menor elemento do restante da lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Troca a posição atual com o menor encontrado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return lista

import numpy as np

array = np.array([15, 34, 8, 3])
array_ordem_inversa = np.array([10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]) # pior caso para Big-O

print(selection_sort(array))

print(selection_sort(array_ordem_inversa))

print()

print(selection_sort2(array))

print(selection_sort2(array_ordem_inversa))
