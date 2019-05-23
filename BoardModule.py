#Representação do tabuleiro e movimentação básica do tabuleiro (Retirar as peças)
from HelpModule import CreateMatrix         #Importa o módulo de criação de matriz

class Position:                             #Classe posição
    def __init__(self, row, col):
        self._row = row
        self._col = col
    
    @property                               #Método GET 'Row'
    def row(self):
        return self._row
    @row.setter                             #Método SET 'Row'
    def row(self, row):
        self._row = row
    
    @property                               #Método GET 'Col'
    def col(self):
        return self._col
    @col.setter                             #Método SET 'Col'
    def col(self, row):
        self._col = col

    def __str__(self):
        return f'{self.row},{self.col}'

class Color:                                #Classe com as cores das peças
    
    @property
    def preta(self):
        return 'Preta'

    @property
    def branca(self):
        return 'Branca'

class Piece:                                #Classe peça

    def __init__(self, board, color):
        self._position = None
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

class Board:                                        #Classe tabuleiro
    
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

    def putPiece(self, piece, pos):
        self._pieces[pos.row][pos.col] = piece  #Coloca uma 'piece' na matriz de peças na posição 'pos'
        piece.position = pos                    #Modifica a posição da peça para 'pos'
