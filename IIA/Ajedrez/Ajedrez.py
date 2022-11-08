import tkinter as tk
import Estados

class Juego:
    def __init__(self, L_CUADRADO):
        self.gs = Estados.GameState()
        self.L_CUADRADO = L_CUADRADO
        self.imagenes = {}

        self.tablero = tk.Tk()
        self.tablero.title("Chess")
        self.tablero.iconbitmap("./Imagenes/logo.ico")
        # self.tablero.geometry(f"{str(L_CUADRADO * 8)} x {str(L_CUADRADO * 8)}")
        # self.tablero.resizable(0, 0)

        self.interfaz = tk.Canvas(self.tablero)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.tablero.mainloop()

    def dibuja_tablero(self):
        for i in range(8):
            for j in range(8):
                if(i + j) % 2 == 0:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#dfc07f")
                    # self.interfaz.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#ffffff")
                else:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#7a4f37")
                    # self.interfaz.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#000000")

    def cargar_imagenes(self):
        piezas = ["bT", "bC", "bA", "bQ", "bR", "bP", "nT", "nC", "nA", "nQ", "nR", "nP"]
        for ficha in piezas:
            self.imagenes[ficha] = tk.PhotoImage(file="./Imagenes/" + ficha + ".png").zoom(self.L_CUADRADO).subsample(60)
    
    def mostrar_piezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j != "__":
                    self.interfaz.create_image(indice_j*self.L_CUADRADO, indice_i*self.L_CUADRADO, image=self.imagenes[j], anchor="nw")
                    

##  MAIN    ##
chess = Juego(70)
chess.dibuja_tablero()
chess()
chess.cargar_imagenes()
chess.mostrar_piezas()