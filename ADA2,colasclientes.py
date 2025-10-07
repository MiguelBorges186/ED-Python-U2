
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)


class Servicio:
    def __init__(self):
        self.cola = Cola()
        self.next_ticket = 1 

    def nuevo_turno(self, prefijo):
        t = f"{prefijo}-{self.next_ticket:03d}"
        self.cola.encolar(t)
        self.next_ticket += 1
        return t

    def atender(self):
        return self.cola.desencolar()


def _num_servicio(texto):
    dig = "".join(ch for ch in texto if ch.isdigit())
    return int(dig) if dig else None


servicios = {}  

print("Sistema de colas (C<serv>, A<serv>, Q/SALIR)")

while True:
    cmd = input("> ").strip()
    if not cmd:
        continue

    up = cmd.upper()
    if up in ("Q", "SALIR"):
        print("Fin.")
        break

    op = up[0]
    s = _num_servicio(cmd)
    if op not in ("C", "A") or s is None:
        print("Formato: C1, C 2, A1, A 3, Q")
        continue

    if s not in servicios:
        servicios[s] = Servicio()

    if op == "C":
        turno = servicios[s].nuevo_turno(f"S{s}")
        print(f"Turno asignado: {turno}")
    else:  
        turno = servicios[s].atender()
        if turno is None:
            print(f"Servicio {s}: sin clientes.")
        else:
            print(f"Llamando: {turno}")
