import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self, canvas):
        self.items = []
        self.canvas = canvas
        self.altura = 50     
        self.ancho  = 120    
        self.gap    = 6      

    def dibujar(self):
        self.canvas.delete("all")
        x0, y0 = 140, 40  

        for i, elem in enumerate(reversed(self.items)):
            y_top = y0 + i * (self.altura + self.gap)
            x1 = x0 + self.ancho
            color = "#fca5a5" if i == 0 else "#93c5fd"
            self.canvas.create_rectangle(x0, y_top, x1, y_top + self.altura,
                                         fill=color, outline="#111827")
            self.canvas.create_text(x0 + self.ancho/2, y_top + self.altura/2,
                                    text=str(elem), font=("Arial", 13, "bold"))
        if self.items:
            self.canvas.create_text(x0 - 35, y0 + self.altura/2,
                                    text="CIMA ↑", font=("Arial", 10, "bold"))

    def apilar(self, elemento):
        self.items.append(elemento)  
        self.dibujar()

    def desapilar(self):
        if self.items:
            elem = self.items.pop()   
            self.dibujar()
            return elem
        messagebox.showwarning("Atención", "La pila está vacía")
        return None

    def cima(self):
        return self.items[-1] if self.items else None

def main():
    ventana = tk.Tk()
    ventana.title("Pila (cima arriba)")
    ventana.geometry("450x420")

    canvas = tk.Canvas(ventana, width=430, height=330, bg="white")
    canvas.pack(padx=10, pady=10)

    pila = Pila(canvas)

    frame = tk.Frame(ventana)
    frame.pack(pady=5)

    entrada = tk.Entry(frame, width=12)
    entrada.grid(row=0, column=0, padx=6)

    def apilar():
        v = entrada.get()
        if v:
            pila.apilar(v)
            entrada.delete(0, tk.END)

    def desapilar():
        elem = pila.desapilar()
        if elem is not None:
            messagebox.showinfo("Desapilado", f"Se quitó: {elem}")

    def ver_cima():
        elem = pila.cima()
        messagebox.showinfo("Cima", f"Cima: {elem}" if elem is not None else "Pila vacía")

    tk.Button(frame, text="Apilar",    command=apilar).grid(   row=0, column=1, padx=6)
    tk.Button(frame, text="Desapilar", command=desapilar).grid(row=0, column=2, padx=6)
    tk.Button(frame, text="Ver cima",  command=ver_cima).grid( row=0, column=3, padx=6)

    ventana.mainloop()

if __name__ == "__main__":
    main()
