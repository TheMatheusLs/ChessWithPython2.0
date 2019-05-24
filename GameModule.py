#Inteligência do jogo de xadrez, como as peças vão se movimentação. Mecanica do jogo
from BoardModule import *           #Importa o módulo das peças

class Tower(Piece):                 #Classe com as regras da 'torre' e herda da classe Peça
    
    def __str__(self):
        return 'T'                  #Imprime a 'Torre' como um 'T'    
    
class King(Piece):                  #Classe com as regras da 'rei' e herda da classe Peça
    
    def __str__(self):
        return 'K'                  #Imprime a 'Rei' como um 'R' 

class ChessPositon:

    def __init__(self, col, row):
        self._col = col
        self._row = row

    @property
    def col(self):
        return self._col
    @col.setter
    def col(self,col):
        self._col = col
    
    @property
    def row(self):
        return self._row
    @row.setter 
    def row(self, row):
        self._row = row

    def toPosition(self):
        aux = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        return Position(8-self.row, aux[self.col.lower()])

    def __str__(self):
        return f'{self.col.upper()}{self.row}'     

class ChessGame:
    def __init__(self):
        self._board = Board(8,8)
        self._currentPlayer = Color.BRANCA
        self._shift = 1
        self._finish = False
        self.putPiecesInit()

    @property
    def finish(self):
        return self._finish

    @property
    def board(self):
        return self._board

    def putPiecesInit(self):
        self.board.putPiece(Tower(self.board,Color.BRANCA),ChessPositon('c',1).toPosition())  
        self.board.putPiece(Tower(self.board,Color.BRANCA),ChessPositon('c',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.BRANCA),ChessPositon('d',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.BRANCA),ChessPositon('e',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.BRANCA),ChessPositon('e',1).toPosition())
        self.board.putPiece(King(self.board,Color.BRANCA),ChessPositon('d',1).toPosition())

        self.board.putPiece(Tower(self.board,Color.PRETA),ChessPositon('c',7).toPosition())  
        self.board.putPiece(Tower(self.board,Color.PRETA),ChessPositon('c',8).toPosition())
        self.board.putPiece(Tower(self.board,Color.PRETA),ChessPositon('d',7).toPosition())
        self.board.putPiece(Tower(self.board,Color.PRETA),ChessPositon('e',7).toPosition())
        self.board.putPiece(Tower(self.board,Color.PRETA),ChessPositon('e',8).toPosition())
        self.board.putPiece(King(self.board,Color.PRETA),ChessPositon('d',8).toPosition())
    def makeMove(self, origin, destiny):
        p = self.board.removePiece(origin)     #Remove a peça da origem e salva em 'p'
        p.increaseMovement()                    #Acrescenta o movimento da peça 'p'

        p_catch = self.board.removePiece(destiny)  #Remove a peça do destino e salva em p_catch
        self.board.putPiece(p,destiny)             #Coloca a pela da origem no destino


    

