class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def prioridad(op):
    if op == '^': return 3
    if op in ('*', '/'): return 2
    if op in ('+', '-'): return 1
    return 0

def construir_arbol(expresion):
    operandos = []   
    operadores = []  
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():  
            operandos.append(Nodo(token))
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores[-1] != '(':
                crear_subarbol(operandos, operadores)
            operadores.pop() 
        else:  
            while (operadores and operadores[-1] != '(' and
                  ((token != '^' and prioridad(operadores[-1]) >= prioridad(token)) or
                   (token == '^' and prioridad(operadores[-1]) > prioridad(token)))):
                crear_subarbol(operandos, operadores)
            operadores.append(token)

    while operadores:
        crear_subarbol(operandos, operadores)

    return operandos[-1]  

def crear_subarbol(operandos, operadores):
    nodo = Nodo(operadores.pop())
    nodo.der = operandos.pop()
    nodo.izq = operandos.pop()
    operandos.append(nodo)

def a_infija(nodo):
    if not nodo.izq and not nodo.der:  
        return nodo.valor
    return f"{a_infija(nodo.izq)} {nodo.valor} {a_infija(nodo.der)}"

def a_postfija(nodo):
    if not nodo.izq and not nodo.der:
        return nodo.valor
    return f"{a_postfija(nodo.izq)} {a_postfija(nodo.der)} {nodo.valor}"

def a_prefija(nodo):
    if not nodo.izq and not nodo.der:
        return nodo.valor
    return f"{nodo.valor} {a_prefija(nodo.izq)} {a_prefija(nodo.der)}"


print("Escribe la expresión en notación infija (usa espacios entre números y operadores).")
expresion = input("Tu expresión: ")

arbol = construir_arbol(expresion)

print("\nExpresión Infija :", a_infija(arbol))
print("Expresión Postfija:", a_postfija(arbol))
print("Expresión Prefija :", a_prefija(arbol))
