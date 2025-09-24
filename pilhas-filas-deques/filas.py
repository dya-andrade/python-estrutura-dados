import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__final = -1
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __fila_vazia(self):
        return self.__numero_elementos == 0

    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        self.__final = (self.__final + 1) % self.__capacidade  # 4 + 1 = 5 -> 5 % 5 = 0 ou final < capacidade == final
        self.__valores[self.__final] = valor
        self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia!')
            return None

        temp = self.__valores[self.__inicio]

        self.__inicio = (self.__inicio + 1) % self.__capacidade  # 4 + 1 = 5 -> 5 % 5 = 0 ou final < capacidade == final
        self.__numero_elementos -= 1

        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.__valores[self.__inicio]

fila = FilaCircular(5)

print(fila.primeiro())

fila.enfileirar(1)

print(fila.primeiro())

fila.enfileirar(5)

print(fila.primeiro())

fila.enfileirar(4)
fila.enfileirar(2)
fila.enfileirar(3)

fila.enfileirar(6)

print(fila.primeiro())

print(fila.desenfileirar())

print(fila.primeiro())

print(fila.desenfileirar())

print(fila.primeiro())