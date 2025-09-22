import numpy as np

class VetorNaoOrdenado:
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

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # Linear - O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
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

vetor = VetorNaoOrdenado(5)

vetor.imprime()

vetor.insere(2)

vetor.imprime()

vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

vetor.imprime()

vetor.insere(7)

print(vetor.ultima_posicao)

vetor5 = vetor.pesquisar(5) # O(3)
print(vetor5)

vetorNaoExiste = vetor.pesquisar(4) # O(5)
print(vetorNaoExiste)

vetor2 = vetor.pesquisar(2) # O(1)
print(vetor2)

vetor.excluir(5)

vetor.imprime()

print(vetor.excluir(5))

vetor.excluir(3)

vetor.imprime()

vetor.insere(6)

vetor.imprime()

