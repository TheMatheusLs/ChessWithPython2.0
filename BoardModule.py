#Representação do tabuleiro e movimentação básica do tabuleiro (Retirar as peças)
from HelpModule import CreateMatrix
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

class Collor:
    def Collor(self):
        colorList = ['Branca','Preta','Vermelho'] 
        return colorList

class Piece:

    def __init__(self, position, board, color):
        self._position = position
        self._board = board
        self._color = color
        self._move_count = 0

    @property
    def position(self):
        return self._position
    @position.setter 
    def position(self, position):
        self._position = position

    @property
    def color(self):
        return self._color

    @property
    def move_count(self):
        return self._move_count
    
    @property
    def board(self):
        return self._board

class Board:
    
    def __init__(self, row=8, col=8):
        self._row = row
        self._col = col
        self._pieces = CreateMatrix(row,col,None)

    @property
    def row(self):
        return self._row
    @property
    def col(self):
        return self._col
    
    def piece(self, row, col):
        return self._pieces[row][col]
