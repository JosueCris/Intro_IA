pawn = 1   # peon       # 8 blancas - 8 negras
knight = 3 # caballo    # 2 blancas - 2 negras
bishop = 3 # alfil      # 2 blancas - 2 negras
castle = 5 # torre      # 2 blancas - 2 negras
queen = 9  # reina      # 1 blancas - 1 negras
king = 4   # rey        # 1 blancas - 1 negras

class Chess:
    def __init__(self, pieza):
        self.pieza = pieza
        self.hijos = []

    def casilla_objetivo(self, meta):
        return self.pieza == meta

    def mueve_peon(self):
        pass

    def mueve_caballo(self):
        pass

    def mueve_alfil(self):
        pass

    def mueve_torre(self):
        pass

    def mueve_reina(self):
        pass

    def mueve_rey(self):
        pass

    def DFS(self):
        pass
