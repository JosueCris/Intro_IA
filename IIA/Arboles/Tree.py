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
    
    def more_to_right(self):
        if not self:
            return None
        if not self.right:
            return self
        return self.right.more_to_right()

    def more_to_left(self):
        if not self:
            return None
        if not self.left:
            return self
        return self.left.more_to_left()

    # def delete(self, data):
    #     if not self:
    #         return None
    #     item = self.search(data)
    #     if data is item.data:
    #         aux = self
            
    #     if data < item.data:
    #         self.left.delete(data)
    #     if data > item.data:
    #         self.right.delete(data)
       
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
        return self.right.height() - self.left.height()

    def lsr(self):
        if not self:
            return 0
        factor = self.balance_factor()
        if factor < 0:
            aux = self.right
            self.right = self
            self = aux
        return 1

    def rsr(self):
        if not self:
            return 0
        factor = self.balance_factor()
        if factor > 0:
            if self.right:
                aux = self.left
                aux.left = self
                self = aux
        return 1
        
    def lcr(self):
        if not self:
            return 0
        aux1 = self.left
        aux2 = aux1.right
        aux1.right = aux2.left
        self.left = aux2.right
        aux2.right = self
        self = aux2
        return 1

    def rcr(self):
        if not self:
            return 0
        aux1 = self.left
        aux2 = aux1.right
        aux1.right = aux2.left
        self.left = aux2.right
        aux2.right = self
        self = aux2
        return 1