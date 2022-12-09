class Nodo:
    def __init__(self, dato):
        self.dato:str = dato
        self.siguiente = None

    def imprimirNodo(self):
        return self.dato + ", "

class Cola:
    head = Nodo

    def __init__(self):
        self.head = None

    def insertar(self, n):
        if self.head is None:
            self.head = n
            return
        h = self.head
        while h.siguiente is not None:
            h = h.siguiente
        h.siguiente = n

    def imprimir(self):
        h = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo()
            h = h.siguiente
        return cadena

if __name__ == '__main__':
    end = 0
    p: Cola = Cola()
    while end == 0:
        print("Ingresa un numero: ")
        dato = input()
        if dato.upper() == "i":
            print(p.imprimir())
        else:
            n = Nodo(dato)
            p.insertar(n)
            print(p.imprimir())
