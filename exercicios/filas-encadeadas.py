class No:
    def __init__(self, valor):
        self.__valor = valor
        self.proximo = None

    def valor(self):
        print(self.__valor)

class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def __fila_vazia(self):
        return self.__inicio is None

    def enfileirar_inicio(self, valor):
        novo = No(valor)

        if self.__fila_vazia():
            self.__inicio = novo
            self.__final = novo
        else:
            novo.proximo = self.__inicio
            self.__inicio = novo

    def enfileirar_final(self, valor):
        novo = No(valor)

        if self.__fila_vazia():
            self.__inicio = novo
            self.__final = novo
        else:
            self.__final.proximo = novo
            self.__final = novo

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A lista está vázia!")
            return None

        temp = self.__inicio

        if self.__inicio == self.__final:
            self.__inicio = None
            self.__final = None
        else:
            self.__inicio = self.__inicio.proximo

        temp.proximo = None

        return temp

    def ver_inicio(self):
        return self.__inicio

# Outra forma: https://colab.research.google.com/drive/1RTrkpgZ1H_k3EbPVaIiBRfHmMSyjDuOZ?usp=sharing

fila = FilaEncadeada()

fila.enfileirar_inicio(5)
fila.enfileirar_final(4)
fila.enfileirar_final(8)

fila.ver_inicio().valor()

fila.enfileirar_inicio(1)

fila.ver_inicio().valor()

fila.desenfileirar()

fila.ver_inicio().valor()