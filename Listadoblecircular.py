class Nodo:

    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LIsta_Circular_Doble_Enlazada:

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def add_Final(self, valor):
        MyNode = Nodo(valor)

        if self.vacia() == True:
            self.primero = MyNode
            self.ultimo = MyNode
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = MyNode
            self.ultimo.anterior = aux

        self.__unir_nodos()

    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer_inicio_fin(self):

        aux = self.primero

        while aux != None:
            print(aux.valor)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def buscar(self, valor):
        aux = self.primero

        while aux != None:
            if aux.valor == valor:
                print("Anterior: %s" % (aux.anterior.valor))
                print("actual: %s" % (aux.valor))
                print("Siguiente: %s" % (aux.siguiente.valor))

            if aux.siguiente == self.primero:
                return

            aux = aux.siguiente


lista = LIsta_Circular_Doble_Enlazada()

lista.add_Final(1)
lista.add_Final(2)
lista.add_Final(3)
lista.add_Final(4)
lista.add_Final(5)
lista.recorrer_inicio_fin()

lista.buscar(5)
