import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __fila_vazia(self):
        return self.__numero_elementos == 0

    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia!')
            return
        if self.__numero_elementos == 0:
            self.__valores[self.__numero_elementos] = valor
            self.__numero_elementos += 1
        else:
            x = self.__numero_elementos - 1
            while x >= 0:
                if valor > self.__valores[x]:
                    self.__valores[x + 1] = self.__valores[x]
                else:
                    break
                x -= 1

            self.__valores[x + 1] = valor
            self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vázia!')
            return

        valor = self.__valores[self.__numero_elementos - 1]
        self.__numero_elementos -= 1
        return valor

    def ver_primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.__valores[self.__numero_elementos - 1]

fila = FilaPrioridade(5)

print(fila.ver_primeiro())

fila.enfileirar(30)
fila.enfileirar(15)
fila.enfileirar(45)

print(fila.ver_primeiro())

fila.enfileirar(40)

fila.desenfileirar()
fila.desenfileirar()