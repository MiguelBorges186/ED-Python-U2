import tkinter as tk
from tkinter import messagebox

class HanoiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi ")
        self.root.geometry("600x420")
        self.root.config(bg="#f2f2f2")

        self.num_discos = 3
        self.torres = [[], [], []]
        self.torre_seleccionada = None
        self.movimientos = 0
        self.completado = False  

        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="white")
        self.canvas.pack(pady=20)

        frame_botones = tk.Frame(self.root, bg="#f2f2f2")
        frame_botones.pack()
        tk.Button(frame_botones, text="Torre A", command=lambda: self.torre_click(0), width=10).grid(row=0, column=0, padx=15)
        tk.Button(frame_botones, text="Torre B", command=lambda: self.torre_click(1), width=10).grid(row=0, column=1, padx=15)
        tk.Button(frame_botones, text="Torre C", command=lambda: self.torre_click(2), width=10).grid(row=0, column=2, padx=15)

        self.label_movs = tk.Label(self.root, text="Movimientos: 0", font=("Arial", 12), bg="#f2f2f2")
        self.label_movs.pack(pady=5)

        self.reiniciar_juego()

    def reiniciar_juego(self):
        """Reinicia el juego"""
        self.torres = [[3, 2, 1], [], []]
        self.movimientos = 0
        self.torre_seleccionada = None
        self.completado = False
        self.actualizar_pantalla()

    def torre_click(self, indice):
        """Selecciona torre origen/destino"""
        if self.completado:
            return  

        if self.torre_seleccionada is None:
            if not self.torres[indice]:
                messagebox.showinfo("Aviso", "La torre está vacía.")
                return
            self.torre_seleccionada = indice
        else:
            if indice == self.torre_seleccionada:
                self.torre_seleccionada = None
                return
            self.mover_disco(self.torre_seleccionada, indice)
            self.torre_seleccionada = None

    def mover_disco(self, origen, destino):
        """Mueve disco si es válido"""
        if not self.torres[origen]:
            return
        disco = self.torres[origen][-1]
        if not self.torres[destino] or disco < self.torres[destino][-1]:
            self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos += 1
            self.actualizar_pantalla()
            self.verificar_ganador()
        else:
            messagebox.showwarning("Movimiento inválido", "No puedes poner un disco grande sobre uno pequeño.")

    def actualizar_pantalla(self):
        """Dibuja las torres y discos"""
        self.canvas.delete("all")
        torre_x = [130, 300, 470]
        base_y = 250
        alto = 22

        for x in torre_x:
            self.canvas.create_rectangle(x - 5, 120, x + 5, base_y, fill="#8B4513")

        colores = ["#ffcc00", "#4caf50", "#2196f3", "#9c27b0", "#ff5252"]
        for i in range(3):
            torre = self.torres[i]
            for nivel, disco in enumerate(torre):
                ancho = 40 + (disco - 1) * 30
                x = torre_x[i]
                y_bottom = base_y - nivel * alto
                y_top = y_bottom - alto
                self.canvas.create_rectangle(x - ancho/2, y_top, x + ancho/2, y_bottom,
                                            fill=colores[(disco-1) % len(colores)], outline="black")

        if self.completado:
            self.canvas.create_text(300, 80, text=" ¡Completado!", font=("Arial", 20, "bold"), fill="green")

        self.label_movs.config(text=f"Movimientos: {self.movimientos}")

    def verificar_ganador(self):
        """Verifica si todos los discos están en la torre C"""
        if len(self.torres[2]) == self.num_discos:
            self.completado = True
            self.actualizar_pantalla()
            messagebox.showinfo("¡Listo!", f"Completaste el juego en {self.movimientos} movimientos 🎉")

root = tk.Tk()
app = HanoiApp(root)
root.mainloop()
