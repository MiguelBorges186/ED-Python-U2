class Cola:

    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not self.items

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
    
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def __str__(self):
        return str(self.items)

def sumar_colas(cola_a, cola_b):

    cola_resultado = Cola()
    while not cola_a.esta_vacia():
        num1 = cola_a.desencolar()
        num2 = cola_b.desencolar()
        suma = num1 + num2
        cola_resultado.encolar(suma)
    return cola_resultado


def llenar_cola_interactiva(nombre_cola, tamano):

    print(f"\n Llenando la {nombre_cola} ")
    cola = Cola()
    for i in range(tamano):
        while True:
            try:
                numero = int(input(f"Introduce el elemento {i + 1} de {tamano}: "))
                cola.encolar(numero)
                break 
            except ValueError:
                print("Error: Por favor, introduce solo números enteros.")
    return cola

print("--- Suma de dos Colas ---")

while True:
    try:
        tamano_colas = int(input("¿Cuántos elementos quieres en cada cola?: "))
        if tamano_colas > 0:
            break
        else:
            print("Por favor, introduce un número mayor que cero.")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

cola_a = llenar_cola_interactiva("Cola A", tamano_colas)
cola_b = llenar_cola_interactiva("Cola B", tamano_colas)

print("\n--- Colas Originales ---")
print(f"Cola A: {cola_a}")
print(f"Cola B: {cola_b}")
print("-" * 26)

cola_final = sumar_colas(cola_a, cola_b)

print("\n--- Resultado de la Suma ---")
print(f"Cola Resultado: {cola_final}")

print("\n--- Estado final de las Colas Originales ---")
print(f"Cola A después de la operación: {cola_a}")
print(f"Cola B después de la operación: {cola_b}")