##  IMPLEMENTACION DE UN ARBOL BINARIO DE BUSQUEDA
class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Tree(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Tree(data)
        # return self.balance_tree()



    def pre_orden(self):
        print(self.data, "-> ", end="")
        if self.left:
            self.left.pre_orden()
        if self.right:
            self.right.pre_orden()


    def in_orden(self):
        if self.left:
            self.left.in_orden()
        print(self.data, "-> ", end="")
        if self.right:
            self.right.in_orden()


    def post_orden(self):
        if self.left:
            self.left.post_orden()
        if self.right:
            self.right.post_orden()
        print(self.data, "-> ", end="")


    def search(self, data):
        if not self:
            return None
        if data is self.data:
            return self
        if data < self.data:
            if not self.left:
                return None
            return self.left.search(data)
        if data > self.data:
            if not self.right:
                return None
            return self.right.search(data)
    
    
    def rightmost(self):
        if not self:
            return None
        if not self.right:
            return self
        return self.right.rightmost()


    def leftmost(self):
        if not self:
            return None
        if not self.left:
            return self
        return self.left.leftmost()


    def delete(self, data):
        if not self:
            return None
        # Buscamos el nodo a eliminar
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Si lo encontramos, procedemos a eliminarlo
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                # Si el nodo tiene dos hijos, encontrar el sucesor inmediato
                successor = self.right.leftmost()
                self.data = successor.data
                # Eliminar el sucesor inmediato
                self.right = self.right.delete(successor.data)
        return self  # Importante: devolver el nodo actual después de cualquier modificación


    def nodes_cant(self):
        nodes = 1
        if self is None:
            return 0
        if self.left:
            nodes += self.left.nodes_cant()
        if self.right:
            nodes += self.right.nodes_cant()
        return nodes


    def leafs_cant(self): 
        if self is None:
            return 0
        if (self.left is None) or (self.right is None):
            return 1
        return self.left.leafs_cant() + self.right.leafs_cant()


##  Igual se puede usar directo con la funcion max de python pero hice mi propia implementacion del retorno
    def max(self, left, right):
        if left > right:
            return left
        return right


    def height(self):
        left = 1
        right = 1
        if not self:
            return 0
        if self.left:
            left += self.left.height()
        if self.right:
            right += self.right.height()
        return self.max(left, right)


##  Inicio de la pesadilla :'v
    def balance_factor(self):
        if not self:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return right_height - left_height


    def slr(self):
        if not self:
            return None
        if not self.right:
            return None
        aux = self.right
        self.right = aux.left
        aux.left = self
        return aux

    
    def srr(self):
        if not self:
            return None
        if not self.left:
            return None
        aux = self.left
        self.left = aux.right
        aux.right = self
        return aux
    
        
    def clr(self):
        if not self:
            return None
        if not self.right:
            return None
        aux1 = self.right
        aux2 = aux1.left
        aux1.left = aux2.right
        aux2.right = aux1
        self.right = aux1.left
        aux2.left = self
        return aux2


    def crr(self):
        if not self:
            return None
        if not self.left:
            return None
        aux1 = self.left
        aux2 = aux1.right
        aux1.right = aux2.left
        aux2.left = aux1
        self.left = aux1.right
        aux2.right = self
        return aux2
    
    
    def balance_left(self):
        if not self:
            return None
        if not self.left:
            return None
        if not self.left.right:
            return self.srr()
        else:
            return self.crr()


    def balance_right(self):
        if not self:
            return None
        if not self.right:
            return None
        if not self.right.left:
            return self.slr()
        else:
            return self.clr()


    def balance_tree(self):
        if not self:
            return None
        result = self.balance_factor()
        if result < -1:
            return self.balance_left()
        if result > 1:
            return self.balance_right()
        return self