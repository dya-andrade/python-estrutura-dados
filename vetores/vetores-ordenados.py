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
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
           if self.valores[i] > valor:
               return -1
           if self.valores[i] == valor:
               return i
        return -1

    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_esquerda = 0
        limite_direita = self.ultima_posicao

        while limite_esquerda <= limite_direita:
            meio = (limite_esquerda + limite_direita) // 2

            if self.valores[meio] == valor:
                return meio
            elif self.valores[meio] < valor:
                limite_esquerda = meio + 1
            else:
                limite_direita = meio - 1

        return -1  # não encontrado

    # O(log n)
    def pesquisa_binaria_recursiva(self, valor, esquerda, direita):
        # caso base: não encontrado
        if esquerda > direita:
            return -1

        meio = (esquerda + direita) // 2

        if self.valores[meio] == valor:
            return meio
        elif self.valores[meio] < valor:
            # busca na metade direita
            return self.pesquisa_binaria_recursiva(valor, meio + 1, direita)
        else:
            # busca na metade esquerda
            return self.pesquisa_binaria_recursiva(valor, esquerda, meio - 1)

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
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

print(vetor.pesquisa_linear(5))
print(vetor.pesquisa_linear(8))
print(vetor.pesquisa_linear(2))

print(vetor.ultima_posicao)

vetor.excluir(5)
vetor.imprime()
print()

vetor.excluir(1)
vetor.imprime()

print(vetor.excluir(9))

print(vetor.pesquisa_linear(5))
print(vetor.pesquisa_linear(9))

print()

vetor2 = VetorOrdenado(100)

for i in range(0, 100):
    vetor2.insere(i + 1)

vetor2.imprime()

print(vetor2.pesquisa_binaria(33))
print(vetor2.pesquisa_binaria(47))
print(vetor2.pesquisa_binaria_recursiva(47, 0, vetor2.ultima_posicao))