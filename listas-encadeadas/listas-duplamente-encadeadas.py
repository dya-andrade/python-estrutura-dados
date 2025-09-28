class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostrar(self):
        print(self.valor)

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro is None

    def insere_inicio(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            # Se a lista estiver vazia, o novo nó será tanto o primeiro quanto o último
            self.primeiro = novo
            self.ultimo = novo
        else:
            # Caso contrário, o novo nó aponta para o atual primeiro
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
            self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            # Se a lista estiver vazia, o novo nó será tanto o primeiro quanto o último
            self.primeiro = novo
            self.ultimo = novo
        else:
            # Caso contrário, o novo nó aponta para o atual último
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
            self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista está vazia!")
            return None

        temp = self.primeiro

        # Se só existe um elemento, limpar primeiro e último
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            # Desconectar o anterior do próximo
            self.primeiro.proximo.anterior = None
            # Avança o ponteiro do primeiro
            self.primeiro = self.primeiro.proximo

        # Opcional: desconectar o nó removido da lista
        temp.proximo = None

        return temp

    def excluir_final(self):
        if self.__lista_vazia():
            print("A lista está vazia!")
            return None

        temp = self.ultimo

        # Se só existe um elemento, limpar primeiro e último
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            # Desconectar o próximo do anterior
            self.ultimo.anterior.proximo = None
            # Avança o ponteiro do último
            self.ultimo = self.ultimo.anterior

        # Opcional: desconectar o nó removido da lista
        temp.anterior = None

        return temp

    def excluir_posicao(self, valor):
        if self.__lista_vazia():
            print("A lista está vazia!")
            return None

        # Começamos a busca pelo nó a ser removido
        atual = self.primeiro

        # Percorre a lista até encontrar o valor ou chegar ao final
        while atual is not None and atual.__valor != valor:
            atual = atual.proximo

        # Caso não tenha encontrado o valor, retornamos None
        if atual is None:
            return None

        # Se o nó a ser removido for o primeiro
        if atual == self.primeiro:
            self.primeiro = atual.proximo
            if self.primeiro:  # evita erro se a lista ficar vazia
                self.primeiro.anterior = None
        else:
            atual.anterior.proximo = atual.proximo

        # Se o nó a ser removido for o último
        if atual == self.ultimo:
            self.ultimo = atual.anterior
            if self.ultimo:  # evita erro se a lista ficar vazia
                self.ultimo.proximo = None
        else:
            atual.proximo.anterior = atual.anterior

        # Retorna o nó removido (poderia ser só o valor, se preferir)
        return atual

    def listar_frente(self):
        if self.__lista_vazia():
            print('A lista está vázia!')
            return

        atual = self.primeiro

        while atual is not None:
            atual.mostrar()
            atual = atual.proximo

    def listar_tras(self):
        if self.__lista_vazia():
            print('A lista está vázia!')
            return

        atual = self.ultimo

        while atual is not None:
            atual.mostrar()
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()

lista.insere_inicio(3)
lista.excluir_final().mostrar()
print()

lista.insere_inicio(2)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.insere_inicio(1)

lista.listar_frente()

print()

lista.listar_tras()

print()
lista.primeiro.mostrar()

lista.insere_final(6)
lista.insere_final(8)

print()
lista.listar_tras()

print()
lista.excluir_inicio().mostrar()

print()
lista.listar_frente()

print()
lista.excluir_posicao(2).mostrar()

print()
lista.listar_frente()

print()
lista.excluir_posicao(8).mostrar()

print()
lista.listar_frente()

print()
lista.excluir_posicao(5).mostrar()

print()
lista.listar_frente()

print()
lista.excluir_posicao(4).mostrar()

print()
lista.excluir_posicao(6).mostrar()

print()
lista.listar_frente()

print()
print(lista.excluir_posicao(2))