class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None

    def valor(self):
        print(self.__valor)

class PilhaEncadeada:
    def __init__(self):
        self.__topo = None

    def __pilha_vazia(self):
        return self.__topo is None

    def empilhar(self, valor):
        novo = No(valor)
        novo.__proximo = self.__topo
        self.__topo = novo

    def desempilhar(self):
        if self.__pilha_vazia():
            print("Lista vazia!")
            return None

        temp = self.__topo
        self.__topo = self.__topo.proximo
        temp.proximo = None

        return temp

    def ver_topo(self):
        return self.__topo

# Outro exemplo: https://colab.research.google.com/drive/1uleRas-AzT8vHXfwvvfYtf8SbOr4Xrai?usp=sharing

pilha = PilhaEncadeada()

pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(7)

pilha.ver_topo().valor()

pilha.desempilhar().valor()

pilha.ver_topo().valor()
