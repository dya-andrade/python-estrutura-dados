class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def lista_vazia(self):
        return self.primeiro is None

    def listar(self):
        if self.lista_vazia():
            print("Lista vazia!")
            return

        atual = self.primeiro

        while atual is not None:
            atual.mostrar()
            atual = atual.proximo

    def pesquisa_linear(self, valor):
        if self.lista_vazia():
            print("Lista vazia!")
            return None

        atual = self.primeiro

        while atual.valor != valor:
            if atual.proximo is None:
                print('O valor não foi encontrado!')
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_inicio(self):
        if self.lista_vazia():
            print("Lista vazia!")
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo  # aponta para o próximo nó
        temp.proximo = None  # boa prática: desconectar o nó removido

        return temp

    def excluir_posicao(self, valor):
        if self.lista_vazia():
            print("Lista vazia!")
            return None

        atual = self.primeiro
        anterior = None

        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print("O valor não foi encontrado!")
            return None

        # Remover o nó
        if anterior is None:  # caso especial: remover o primeiro nó
            self.primeiro = atual.proximo
        else:
            anterior.proximo = atual.proximo

        atual.proximo = None  # boa prática: desconectar
        return atual


lista = ListaEncadeada()

lista.insere_inicio(1)
lista.insere_inicio(5)
lista.insere_inicio(6)

lista.listar()

print(lista.primeiro)
print(lista.primeiro.proximo)

lista.excluir_inicio()

lista.listar()

lista.excluir_inicio()
lista.primeiro.mostrar()
lista.excluir_inicio()
print(lista.excluir_inicio())

lista.listar()

lista.insere_inicio(1)
lista.insere_inicio(5)
lista.insere_inicio(6)
lista.insere_inicio(4)
lista.insere_inicio(2)
lista.insere_inicio(7)

lista.listar()

valor = lista.pesquisa_linear(6)
valor.mostrar()

print(lista.excluir_posicao(6))
print(lista.excluir_posicao(7))

print(lista.pesquisa_linear(8))

lista.listar()