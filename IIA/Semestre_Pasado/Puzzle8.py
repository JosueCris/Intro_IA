import copy

def deepcopy(mat):
    aux = []
    aux2 = None
    for i in range(len(mat)):
        aux2 = []
        for j in range(len(mat[0])):
            aux2.append(mat[i][j])
        aux.append(aux2)
    return aux

def distancia(pos1, pos2):
	return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1]) 

def heuristica(matriz, pos_dic):
	suma = 0
##	print(matriz)
	for x in range(len(matriz[0])):
		for y in range(len(matriz)):
			suma = suma + distancia([x, y], pos_dic[matriz[x][y]])

	return suma

def calcula_diccionario(meta):
	dic = {}
	for x in range(len(meta[0])):
		for y in range(len(meta)):
			dic[meta[x][y]] = [x, y]
	return dic
    
def posxy(mat):
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if mat[i][j] == "_":
                return i, j
    return 0, 0

class puzzle():
    visitados = []
    camino_final = []
    dic_meta = None

    def __init__(self, estado, padre, meta) -> None:
        self.estado = estado
        self.hijos = []
        self.padre = padre
        self.heuristica = heuristica(estado, puzzle.dic_meta)
        self.meta = meta

    def camino(self):
        if (self.estado == self.meta):
            return self
        x, y = posxy(self.estado)
        self.hijo_arriba(x, y)
        self.hijo_abajo(x, y)
        self.hijo_derecha(x, y)
        self.hijo_izquierda(x, y)

        ord =sorted(self.hijos, key=lambda x: x.heuristica)
        
    def hijo_arriba(self, pos_x, pos_y):
        if pos_y <= 0:
            return
        hijo = copy.deepcopy(self.estado)
        temp = hijo[pos_x][pos_y - 1]
        hijo[pos_x][pos_y-1] = "_"
        hijo[pos_x][pos_y] = temp
        if hijo in puzzle.visitados:
            return
        self.hijos.append(hijo)

    def hijo_abajo(self, pos_x, pos_y):
        if pos_y >= 2:
            return
        hijo = copy.deepcopy(self.estado)
        temp = hijo[pos_x][pos_y + 1]
        hijo[pos_x][pos_y+1] = "_"
        hijo[pos_x][pos_y] = temp
        if hijo in puzzle.visitados:
            return
        self.hijos.append(hijo)
    
    def hijo_derecha(self, pos_x, pos_y):
        if pos_x >= 2:
            return
        hijo = copy.deepcopy(self.estado)
        temp = hijo[pos_x + 1][pos_y]
        hijo[pos_x + 1][pos_y] = "_"
        hijo[pos_x][pos_y] = temp
        if hijo in puzzle.visitados:
            return
        self.hijos.append(hijo)
    
    def hijo_izquierda(self, pos_x, pos_y):
        if pos_x <= 0:
            return
        hijo = copy.deepcopy(self.estado)
        temp = hijo[pos_x - 1][pos_y]
        hijo[pos_x - 1][pos_y] = "_"
        hijo[pos_x][pos_y] = temp
        if hijo in puzzle.visitados:
            return
        self.hijos.append(hijo)
    
        

        
        
        

    
        

mat = [ [1,   2,    3],
		[8,  "_",   7],
		[6,   4,    5] ]

mat2 = [ [1,   2,    3],
		[8,  "_",   7],
		[6,   4,    5] ]

lis = [mat]


print(mat)
print(copy.deepcopy(mat))
print(mat2 in lis)