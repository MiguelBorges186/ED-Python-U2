CAPACIDAD = 8
pila = []

def tope():
    """Devuelve el número de elementos (posición del tope)."""
    return len(pila)

def push(x):
    """Inserta un elemento en la pila."""
    if tope() >= CAPACIDAD:
        print(f" OVERFLOW al intentar insertar {x}")
        return
    pila.append(x)
    print(f" Insertar({x}) realizado con éxito.")
    mostrar_pila()

def pop(etiqueta):
    """Elimina un elemento de la pila."""
    if tope() == 0:
        print(f" UNDERFLOW al intentar eliminar ({etiqueta})")
        return
    eliminado = pila.pop()
    print(f" Eliminar({etiqueta}) → se sacó '{eliminado}'")
    mostrar_pila()

def mostrar_pila():
    """Muestra visualmente el contenido de la pila y el tope."""
    print("\nEstado actual de la pila:")
    for i in range(CAPACIDAD-1, -1, -1):
        if i < tope():
            print(f"| {pila[i]} |")
        else:
            print("|   |")
    print("‾‾‾‾‾")
    print(f"TOPE = {tope()}\n")



print("Simulación de operaciones con PILA \n")

push("X")  # a
push("Y")  # b
pop("Z")   # c
pop("T")   # d
pop("U")   # e
push("V")  # f
push("W")  # g
pop("P")   # h
push("R")  # i

print("=== RESULTADO FINAL ===")
mostrar_pila()
print(f"Elementos finales en la pila: {tope()}")