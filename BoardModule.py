#Representação do tabuleiro e movimentação básica do tabuleiro (Retirar as peças)

class Position:
    
    def __init__(self, row, col):
        self._row = row
        self._col = col
    
    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, row):
        self._row = row
    
    @property
    def col(self):
        return self._col
    @col.setter
    def col(self, row):
        self._col = col

    def __str__(self):
        return f'{self.row},{self.col}'