class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:
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
            novo.proximo = self.primeiro
            self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.primeiro = novo
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista está vázia!")
            return None

        temp = self.primeiro

        # Se só existe um elemento, limpar primeiro e último
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            # Avança o ponteiro do primeiro
            self.primeiro = self.primeiro.proximo

        # Opcional: desconectar o nó removido da lista
        temp.proximo = None

        return temp

    def listar(self):
        if self.__lista_vazia():
            print('A lista está vázia!')
            return

        atual = self.primeiro

        while atual is not None:
            atual.mostrar()
            atual = atual.proximo

lista = ListaEncadeadaExtremidadeDupla()

lista.insere_inicio(5)
lista.insere_inicio(4)
lista.insere_inicio(8)
lista.insere_inicio(3)

lista.listar()

print()

lista.insere_final(9)
lista.insere_final(2)

lista.listar()

print()
lista.ultimo.mostrar()

lista.excluir_inicio()
lista.excluir_inicio()

print()
lista.listar()

