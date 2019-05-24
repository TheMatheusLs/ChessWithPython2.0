#Inteligência do jogo de xadrez, como as peças vão se movimentação. Mecanica do jogo
from BoardModule import *           #Importa o módulo das peças

class Tower(Piece):                 #Classe com as regras da 'torre' e herda da classe Peça
    
    def __str__(self):
        return 'T'                  #Imprime a 'Torre' como um 'T'    
    
    def canMove(self, pos):
        p = self.board.piece(pos)
        return p == None or p.color is not self.color

    def possibleMoves(self):
        mat = CreateMatrix(self.board.row, self.board.col, None)

        pos = Position(0,0)

        #acima
        pos.setterValues(self.position.row - 1, self.position.col)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.row -= 1
        #Abaixo
        pos.setterValues(self.position.row + 1, self.position.col)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.row += 1  
        #Direita
        pos.setterValues(self.position.row, self.position.col + 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.col += 1  
        #Esquerda
        pos.setterValues(self.position.row, self.position.col - 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.col -= 1 
        return mat

class King(Piece):                  #Classe com as regras da 'rei' e herda da classe Peça
    
    def __str__(self):
        return 'K'                  #Imprime a 'Rei' como um 'R' 

    def canMove(self, pos):
        p = self.board.piece(pos)
        return (p == None) or p.color != self.color

    def possibleMoves(self):
        mat = CreateMatrix(self.board.row, self.board.col, None)

        pos = Position(0,0)

        #acima
        pos.setterValues(self.position.row - 1, self.position.col)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #nordeste
        pos.setterValues(self.position.row - 1, self.position.col+1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Direita
        pos.setterValues(self.position.row , self.position.col+1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Suldeste
        pos.setterValues(self.position.row +1, self.position.col+1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Abaixo
        pos.setterValues(self.position.row+1, self.position.col)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Sudoeste
        pos.setterValues(self.position.row + 1, self.position.col-1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Esquerda
        pos.setterValues(self.position.row, self.position.col-1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        #Noroeste
        pos.setterValues(self.position.row - 1, self.position.col - 1)
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        return mat
    
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
        self._currentPlayer = Color.WHITE
        self._shift = 1
        self._finish = False
        self.putPiecesInit()

    @property
    def shift(self):
        return self._shift

    @property
    def currentPlayer(self):
        return self._currentPlayer

    @property
    def finish(self):
        return self._finish

    @property
    def board(self):
        return self._board       

    def putPiecesInit(self):
        self.board.putPiece(Tower(self.board,Color.WHITE),ChessPositon('c',1).toPosition())  
        self.board.putPiece(Tower(self.board,Color.WHITE),ChessPositon('c',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.WHITE),ChessPositon('d',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.WHITE),ChessPositon('e',2).toPosition())
        self.board.putPiece(Tower(self.board,Color.WHITE),ChessPositon('e',1).toPosition())
        self.board.putPiece(King(self.board,Color.WHITE),ChessPositon('d',1).toPosition())

        self.board.putPiece(Tower(self.board,Color.BLACK),ChessPositon('c',7).toPosition())  
        self.board.putPiece(Tower(self.board,Color.BLACK),ChessPositon('c',8).toPosition())
        self.board.putPiece(Tower(self.board,Color.BLACK),ChessPositon('d',7).toPosition())
        self.board.putPiece(Tower(self.board,Color.BLACK),ChessPositon('e',7).toPosition())
        self.board.putPiece(Tower(self.board,Color.BLACK),ChessPositon('e',8).toPosition())
        self.board.putPiece(King(self.board,Color.BLACK),ChessPositon('d',8).toPosition())

    def makeAMove(self,origin, destiny):
        self.makeMove(origin, destiny)
        self._shift += 1
        self.changePlayer()

    def validateOriginPosition(self, pos):
        if self.board.piece(pos) == None:
            raise BoardException("Não existe peça na posição de origem escolhida!")
        if self.currentPlayer != self.board.piece(pos).color:
            raise BoardException("A peça de origem escolhida não é sua!")
        if not self.board.piece(pos).thereIsMovementPossible():
            raise BoardException("Não há movimentos disponíveis para a peça escolhida!")

    def validateOriginDestiny(self, origin, destiny):
        if not self.board.piece(origin).canMoveTo(destiny):
            raise BoardException("Posição de destino inválida!")


    def changePlayer(self):
        if self._currentPlayer == Color.WHITE:
            self._currentPlayer = Color.BLACK
        else:
            self._currentPlayer = Color.WHITE

    def makeMove(self, origin, destiny):
        p = self.board.removePiece(origin)     #Remove a peça da origem e salva em 'p'
        p.increaseMovement()                    #Acrescenta o movimento da peça 'p'

        p_catch = self.board.removePiece(destiny)  #Remove a peça do destino e salva em p_catch
        self.board.putPiece(p,destiny)             #Coloca a pela da origem no destino


    

