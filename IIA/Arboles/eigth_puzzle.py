import copy
import math
import sys
sys.setrecursionlimit(2169)

visited = []
visit = []
queue = []


def get_num(matriz, num):
    row = 0
    for i in matriz:
        try:
            colum = i.index(num)
            return row, colum
        except:
            row += 1
    return None, None

class Puzzle:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.branches = []

    def is_goal(self, goal):
        return self.state == goal

## Expandimos los movimientos a partir de la posicion del espacio
    def expand(self):
        # if self.is_visited():
        #     return
        # visited.append(self)

        row, colum = self.get_position()
        if not row:
            raise ValueError
        ##  Mover espacio hacia arriba
        if row > 0:
            up = copy.deepcopy(self.state) #para copiar valores y no la direccion de memoria
            up[row - 1][colum] = self.state[row][colum]
            up[row][colum] = self.state[row - 1][colum]
            self.branches.append(Puzzle(up))
        ##  Mover espacio hacia la derecha
        if colum < 2:
            right = copy.deepcopy(self.state) 
            right[row][colum + 1] = self.state[row][colum]
            right[row][colum] = self.state[row][colum + 1]
            self.branches.append(Puzzle(right))
        ##  Mover espacio hacia abajo
        if row < 2:
            down = copy.deepcopy(self.state) #para copiar valores y no la direccion de memoria
            down[row + 1][colum] = self.state[row][colum]
            down[row][colum] = self.state[row + 1][colum]
            self.branches.append(Puzzle(down))            
        ##  Mover espacio hacia la derecha
        if colum > 0:
            left = copy.deepcopy(self.state) 
            left[row][colum - 1] = self.state[row][colum]
            left[row][colum] = self.state[row][colum - 1]
            self.branches.append(Puzzle(left))

##  Obtenemos la posicion donde se encuentra el espacio
    def get_position(self):
        r = 0
        c = 0
        for row in self.state:
            for colum in row:
                if colum == '_':
                    return r, c
                c += 1
            r += 1
            c = 0
        return None, None
    
    def state_print(self):
        for row in self.state:
            for colum in row:
                print(colum, end="   ")
            print(" ")
        print(" ") 

    def is_visited(self):
        return self in visited 

    def DFS(self, goal):
        if not self.state:
            return None
        if self.is_visited():
            return None
        stack = []
        if self.is_goal(goal):
            stack.append(self.state)
            return stack
        visited.append(self.state)
        self.expand()
        for branch in self.branches:
            aux = branch.DFS(goal)
            if aux:
                stack.append(self.state)
                stack.extend(aux)
                return stack
        return stack

## Distancia de Manhatthan
    # def heuristic(self, goal):
    #     value = 0
    #     re = ce = rm = cm = 0
    #     for i in range(8):
    #         rm, cm = goal.get_num(i + 1)
    #         re, ce = self.get_num(i + 1)
    #         value += math.sqrt(math.pow((rm - re), 2)) + math.sqrt(math.pow((cm - ce), 2))
    #     # rm, cm = goal.get_num('_')
    #     # re, ce = self.get_num('_')
    #     # value += math.sqrt(math.pow((rm - re), 2)) + math.sqrt(math.pow((cm - ce), 2))
    #     return value

    def heuristic(self, goal):
        h = 0
        for num in range(1, 9):
            re, ce = get_num(self.state, num)
            rm, cm = get_num(goal, num)
            manhatthan = abs(re - rm) + abs(ce - cm)
            h += manhatthan
        return h

    def greedy_expand(self, goal):
        if self.state == goal:
            return self
        for mat in visited:
            if mat == self.state:
                return None
        visited.append(self.state)
        self.expand()
# Agregar a la franja los hijos ordenados por h
        for branch in self.branches:
            h = branch.heuristic(goal)
            pos = 0
            for nodo in visit:
                if h < nodo.heuristic(goal):
                    break
                pos += 1
            visit.insert(pos, branch)

    def greedy_search(self, goal):
        way = []
        visit.append(self)
# Buscar en el primero de la franja        
        while not visit == []:
            first = visit.pop(0)
            print("**", first.state)
            ret = first.greedy_expand(goal)
            if ret:
                # Regresar el camino
                way.append(ret)
                parent = ret.parent
                while parent:
                    way.append(parent)
                    parent = parent.parent
                print("Solucion encontrada")
                return way
        return None



    def camino_mas_corto(self, meta):
        lessHeur = 0
        masCorto = None
        cont = 0
        for i in self.branches:
            if (cont == 0):
                lessHeur = i.heuristic(meta)
                masCorto = i
            if(i.heuristic(meta) == 0):
                print("Solucion encontrada")
                i.state_print()
                return
            if(i.heuristic(meta) < lessHeur):
                lessHeur = i.heuristic(meta)
                masCorto = i
            cont += 1
        return masCorto.expand("_", meta)
    
    def BFS(self, goal):
        # if self.is_goal(goal):
        #     queue.append(self.state)
        #     return True
        # self.expand()
        # for branch in self.branches:
        #     branch = branch.BFS(goal)
        #     if branch:
        #         branch.append(branch)
        #         return branch
        # return None	
        if not self.state:
            return None 
        if self.is_visited():
            visited.append(self.state)
            return None
        self.expand()
        if self.is_goal(goal):
            queue.append(self.state)
            return queue
        visited.append(self.state)
        self.expand()
        for branch in self.branches:
            collect = branch.BFS(goal)
            if collect:
                collect.append(branch)
                return collect
        return None


##	Implementacion propia del deepcopy
def deepcopy(mat):
    aux = []
    aux2 = None
    for i in range(len(mat)):
        aux2 = []
        for j in range(len(mat[0])):
            aux2.append(mat[i][j])
        aux.append(aux2)
    return aux





## MAIN ##
estado1 = [
                [3,   1,   6],
                [4,  '_',  8],
                [7,   5,   2]
]

estado2 = [
                [7,   1,   6],  
                [4,  '_',  8],
                [3,   5,   2]
] 

meta = [
                [1,   2,   3],
                [4,   5,   6],
                [7,   8, '_']
]

meta2 = [
                [1,   2,   3],
                [8,  '_',  4],
                [7,   6,   5]
]

raiz1 = Puzzle(estado1)
raiz2 = Puzzle(estado2)
final = Puzzle(meta)

# raiz2.expand()
# for lista in raiz2.branches:
#     lista.state_print()


print(f"Suma recorrido: {raiz2.heuristic(meta)}")
numero = 8
print(f"Posicion del {numero}: {get_num(raiz2.state, numero)}")
print("Estado inicial")
raiz2.state_print()


raiz2.greedy_search(final)

# recorrido = raiz2.BFS(meta)
# print(recorrido)
# recorrido.reverse()
# for solucion in recorrido:
#     print(solucion)