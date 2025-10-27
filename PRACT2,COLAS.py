
class Node:
    def __init__(self, info):
        self.info = info      
        self.next = None      



class Order:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad

    def print(self):
        print(f"     Cliente: {self.cliente}")
        print(f"     Cantidad: {self.cantidad}")
        print("     ------------")



class LinkedQueue:
    def __init__(self):
        self.top = None     
        self.tail = None      
        self._size = 0      
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        nuevo = Node(info)
        if self.is_empty():
            self.top = self.tail = nuevo
        else:
            
            self.tail.next = nuevo
            
            self.tail = nuevo
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next  
        if self.top is None:      
            self.tail = None
        self._size -= 1
        return info

    def print_info(self):
        print("********* CONTENIDO DE LA COLA *********")
        print(f"   Tamaño actual: {self._size}")
        nodo = self.top
        contador = 1
        while nodo:
            print(f"   ** Elemento {contador}")
            nodo.info.print()
            nodo = nodo.next
            contador += 1
        print("****************************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self._size:
            return None
        nodo = self.top
        for _ in range(pos - 1):
            nodo = nodo.next
        return nodo.info



if __name__ == "__main__":
    cola = LinkedQueue()

    print("¿La cola está vacía al inicio?:", cola.is_empty())  
    print("Tamaño actual:", cola.size())  

    cola.enqueue(Order(20, "Cliente1"))
    cola.enqueue(Order(30, "Cliente2"))
    cola.enqueue(Order(40, "Cliente3"))
    cola.enqueue(Order(50, "Cliente4"))

    print("\n¿La cola está vacía ahora?:", cola.is_empty())  
    print("Tamaño actual:", cola.size())  

    cola.print_info()

    print("\nPrimer elemento (sin eliminar):")
    primero = cola.front()
    if primero:
        primero.print()

    print("\nElemento eliminado (dequeue):")
    eliminado = cola.dequeue()
    if eliminado:
        eliminado.print()

    cola.print_info()

    print("\nTercer elemento en la cola (sin eliminar):")
    tercero = cola.get_nth(3)
    if tercero:
        tercero.print()
    else:
        print("Posición no válida.")

    print("\n¿La cola está vacía al final?:", cola.is_empty())
    print("Tamaño final:", cola.size())

