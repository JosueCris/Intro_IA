import copy

nodo_visitado = []

class Nodo(object):
    
    def __init__(self, dato):
        super(Nodo, self).__init__()
        self.dato = dato
        self.hijo = [] # Lista
    
    def test_objetivo(self, meta):
        return self.dato == meta
    
    def pos_espacio(self):
        contl = 0
        pos_x = - 1
        pos_y = - 1
        for lista in self.dato:
            try:
                pos_y = lista.index("_")
                pos_x = contl
            except Exception as e: 
                pass
            contl = contl + 1
        return pos_x, pos_y
    
    def mover_arriba(self, pos_x, pos_y):
        if pos_x <= 0:
            return None
        hijo = copy.deepcopy(self.dato)
        temp = hijo[pos_x - 1][pos_y]
        hijo[pos_x - 1][pos_y] = "_"
        hijo[pos_x][pos_y] = temp
        self.hijo.append(Nodo(hijo))
    
    def mover_abajo(self, pos_x, pos_y):
        if pos_x >= 2:
            return None
        hijo = copy.deepcopy(self.dato)
        temp = hijo[pos_x + 1][pos_y]
        hijo[pos_x + 1][pos_y] = "_"
        hijo[pos_x][pos_y] = temp
        self.hijo.append(Nodo(hijo))
    
    def mover_der(self, pos_x, pos_y):
        if pos_y >= 2:
            return None
        hijo = copy.deepcopy(self.dato)
        temp = hijo[pos_x][pos_y + 1]
        hijo[pos_x][pos_y + 1] = "_"
        hijo[pos_x][pos_y] = temp
        self.hijo.append(Nodo(hijo))
    
    def mover_izq(self, pos_x, pos_y):
        if pos_y <= 0:
            return None
        hijo = copy.deepcopy(self.dato)
        temp = hijo[pos_x][pos_y - 1]
        hijo[pos_x][pos_y - 1] = "_"
        hijo[pos_x][pos_y] = temp
        self.hijo.append(Nodo(hijo))

    def generar_hijo(self): # Expandir
        # Buscar pos del espacio
        # Ver movimientos permitidos
        # Guardar los movimientos permitidos en los hijos
        posx, posy = self.pos_espacio()
        if (posx == - 1):
            return None
        self.mover_arriba(posx, posy)
        self.mover_der(posx, posy)
        self.mover_abajo(posx, posy)
        self.mover_izq(posx, posy)
    
    def expandir(self):
        if (self.es_visitado()): # Si ya visitamos este nodo
            return
        visitados.append(self)
        self.generar_hijo()
    
    def es_visitado(self):
        for estado in visitados:
            if estado == self.dato:
                return True
        # True si se encuentra en los visitados
        return False
        # False si no
    
    def busqueda_pp(self, meta):
        if (self.test_objetivo(meta)):
            return True # Caminito de la escuela
        self.expandir()
        for hijo in self.hijo:
           if (hijo.busqueda_pp(meta)):
               return True
        return False

raiz = Nodo([[5, 4, 1], [6, "_", 8], [7, 3, 2]])
raiz.generar_hijo()
print(raiz.dato)
for h in raiz.hijo:
    print (h.dato)