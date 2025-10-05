import numpy as np

# n - i - 1 -> garante que não mexemos com os elementos já ordenados no final da lista.

def bubble_sort(vetor):
    n = len(vetor) # 4

    for i in range(n): # 4 - 1 = 3, pois começa com 0
        final_ordenado = n - i - 1 # 4 - 0 - 1 = 3
        for j in range(0, final_ordenado): # 0 até 3
            # esquerda > direita
            if vetor[j] > vetor[j + 1]:
                # 3 passos
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

def bubble_sort2(lista):
    tamanho = len(lista)

    for passagem in range(tamanho):

        final_ordenado = tamanho - passagem - 1

        for indice in range(0, final_ordenado):
            elemento_atual = lista[indice]
            proximo_elemento = lista[indice + 1]

            # esquerda > direita
            if elemento_atual > proximo_elemento:
                # esquerda e direita = direita e esquerda - troca
                lista[indice], lista[indice + 1] = proximo_elemento, elemento_atual
    return lista

array = np.array([15, 34, 8, 3])
array_ordem_inversa = np.array([10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]) # pior caso para Big-O

print(bubble_sort(array))

print(bubble_sort(array_ordem_inversa))

print()

print(bubble_sort2(array))

print(bubble_sort2(array_ordem_inversa))