import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetores está vázio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
            return

        posicao = 0

        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # O(n) - Linear
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
           if self.valores[i] > valor:
               return -1
           if self.valores[i] == valor:
               return i
        return -1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None

vetor = VetorOrdenado(10)

vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)

vetor.imprime()
print()

print(vetor.pesquisar(5))
print(vetor.pesquisar(8))
print(vetor.pesquisar(2))

print(vetor.ultima_posicao)

vetor.excluir(5)
vetor.imprime()
print()

vetor.excluir(1)
vetor.imprime()

print(vetor.excluir(9))

print(vetor.pesquisar(5))
print(vetor.pesquisar(9))

