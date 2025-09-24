import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade # métodos privados
        self.__criar_lista_vazia()

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia!')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vázia!')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if not self.__pilha_vazia():
            return self.__valores[self.__topo]
        else:
            return "-1"

    def __criar_lista_vazia(self):
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=str)
        # Array de chars
        # self.valores = np.chararray(self.capacidade, unicode=True)

    def validador_expressao(self, expressao):
        expressao = str(expressao)

        aberturas_fechamentos = {'{': '}', '(': ')', '[': ']'}

        if not self.__pilha_vazia():
            print('A pilha precisa está vazia!')
            return
        else:
            for char in expressao:
                e_abertura = False

                if char in aberturas_fechamentos.keys():
                    self.empilhar(char)
                    e_abertura = True

                if not e_abertura:
                    if char in aberturas_fechamentos.values():
                        if aberturas_fechamentos[self.ver_topo()] == char:
                            self.desempilhar()
                        else:
                            print('A expressão está incorreta!')
                            break

            if self.__pilha_vazia():
                print('A expressão está correta!')
            else:
                self.__criar_lista_vazia()

#pilha = Pilha(5)

#print(pilha.ver_topo())

#pilha.empilhar(2)
#pilha.empilhar(5)
#pilha.empilhar(6)
#pilha.empilhar(4)

#print(pilha.ver_topo())

#pilha.desempilhar()
#print(pilha.ver_topo())

pilha = Pilha(12)

#pilha.empilhar('a')
#print(pilha.ver_topo())
pilha.validador_expressao('a{b(c[d]e)f}')
pilha.validador_expressao('ab(c[d]e)f')
pilha.validador_expressao('a{b(c[d]ef}')
pilha.validador_expressao('ab(c[d]e)f')