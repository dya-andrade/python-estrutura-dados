import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = -1
        self.__final = 0
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.__inicio == 0 and self.__final == self.__capacidade - 1) or (self.__inicio == self.__final + 1)


    def __deque_vazio(self):
       return self.__inicio == -1 or self.__final < 0

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio!')
            return

        # caso do deque vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0
        else:
            # anda uma posição circularmente para frente
            self.__inicio = (self.__inicio - 1 + self.__capacidade) % self.__capacidade

        self.__valores[self.__inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio!')
            return

        # caso do deque vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0
        else:
            self.__final = (self.__final + 1) % self.__capacidade

        self.__valores[self.__final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vázio!')
            return None

        temp = self.__valores[self.__inicio]

        # caso só tenha 1 elemento
        if self.__inicio == self.__final:
            self.__inicio = -1
            self.__final = -1
        else:
            self.__inicio = (self.__inicio + 1) % self.__capacidade

        return temp

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque já está vázio!')
            return None

        temp = self.__valores[self.__final]

        # caso só tenha 1 elemento
        if self.__inicio == self.__final:
            self.__inicio = -1
            self.__final = -1
        else:
            self.__final = (self.__final - 1 + self.__capacidade) % self.__capacidade

        return temp

    def get_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vázio!')
            return None

        return self.__valores[self.__inicio]

    def get_final(self):
        if self.__deque_vazio():
            print('O deque já está vázio!')
            return None

        return self.__valores[self.__final]

deque = Deque(10)

deque.insere_final(5)
deque.insere_final(4)
deque.insere_inicio(9)
deque.insere_final(7)
deque.insere_inicio(3)

print(deque.get_inicio())
print(deque.get_final())

print(deque.excluir_final())

print(deque.excluir_inicio())

deque.insere_final(2)
deque.insere_final(1)
deque.insere_inicio(8)
deque.insere_inicio(6)
deque.insere_inicio(13)
deque.insere_inicio(14)
deque.insere_inicio(10)
deque.insere_inicio(15)

print(deque.get_final())