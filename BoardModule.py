#Representação do tabuleiro e movimentação básica do tabuleiro (Retirar as peças)
from HelpModule import CreateMatrix         #Importa o módulo de criação de matriz
#from GameModule import *
from enum import Enum
import abc

class Position:                             #Classe posição
    def __init__(self, row, col):
        self._row = row
        self._col = col
    
    def setterValues(self, row, col):
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
    def col(self, col):
        self._col = col

    def __str__(self):
        return f'{self.row},{self.col}'

class Color(Enum):                          #Classe com as cores das peças
    WHITE = 'White'
    BLACK = 'Black'

class Piece(abc.ABC):                                #Classe peça

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
    
    def increaseMovement(self):
        self._move_count +=1
    
    def decrementMovement(self):
        self._move_count -=1

    @abc.abstractmethod
    def possibleMoves(self):
        pass

    def thereIsMovementPossible(self):
        mat = self.possibleMoves()
        for r in range(self.board.row):
            for c in range(self.board.col):
                if mat[r][c]:
                    return True
        return False

    def  canMoveTo(self, pos):
        return self.possibleMoves()[pos.row][pos.col]


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

    def piece(self, pos):              #Recebe uma posição e retorna a peça localizada naquela posição
        return self._pieces[pos.row][pos.col]

    def thereIsPiece(self, pos):            #Tem uma peça na posição ? 
        self.validatePosition(pos)              #Valida a posição
        return self.piece(pos) is not None      #Retorna se a peça é diferente de None

    def putPiece(self, piece, pos):
        if self.thereIsPiece(pos):
            raise BoardException(f'Já existe uma peça na posição {pos}')    #Lança uma exceção caso já tenha uma peça nessa posição
        self._pieces[pos.row][pos.col] = piece  #Coloca uma 'piece' na matriz de peças na posição 'pos'
        piece.position = pos                    #Modifica a posição da peça para 'pos'

    def removePiece(self, pos):
        if self.piece(pos) == None:
            return None
        aux = self.piece(pos)
        aux.position = None
        self._pieces[pos.row][pos.col] = None
        return aux

    def validPosition(self, pos):      #Verifica a validade da posição, retornando True para uma posição correta
        if pos.row < 0 or pos.row >= self.row or pos.col < 0 or pos.col >= self.col:
            return False
        else:
            return True
    
    def validatePosition(self, pos):
        if not self.validPosition(pos):
            raise BoardException('Posição Inválida!') #Solta uma exceção caso a posição não seja válida

class BoardException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
