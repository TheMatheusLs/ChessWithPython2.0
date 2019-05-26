#Inteligência do jogo de xadrez, como as peças vão se movimentação. Mecanica do jogo
from BoardModule import *           #Importa o módulo das peças

class Rook(Piece):                 
    """
    Classe 'Rook', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'R'                  #Imprime a 'Torre' como um 'T'    
        return '\u2656'                 #imprime o unicode da torre
    def canMove(self, pos):
        p = self.board.piece(pos)
        return p == None or p.color is not self.color

    def possibleMoves(self):
        """
        Cria uma Matriz de possíveis movimentos da 'Torre'.
        \nRetorno:
        \n- Matriz contendo os possíveis movimentos.
        """
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
    """
    Classe 'King', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'K'                  #Imprime a 'Rei' como um 'K' 
        return '\u2654'             #Imprime o unicode do Rei

    def canMove(self, pos):
        p = self.board.piece(pos)
        return (p == None) or p.color != self.color

    def possibleMoves(self):
        """
        Cria uma Matriz de possíveis movimentos do 'Rei'.
        \nRetorno:
        \n- Matriz contendo os possíveis movimentos.
        """
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

class Bishop(Piece):
    """
    Classe 'Bishop', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'B'                  #Imprime o 'Bispo' como um 'B' 
        return '\u265D'             #Imprime o unicode do bispo

    def canMove(self, pos):
        p = self.board.piece(pos)
        return (p == None) or p.color != self.color

    def possibleMoves(self):
        """
        Cria uma Matriz de possíveis movimentos do 'bispo'.
        \nRetorno:
        \n- Matriz contendo os possíveis movimentos.
        """
        mat = CreateMatrix(self.board.row, self.board.col, None)

        pos = Position(0,0)

        #NO
        pos.setterValues(self.position.row - 1, self.position.col - 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row - 1, pos.col -1)
        #NE
        pos.setterValues(self.position.row - 1, self.position.col + 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row - 1, pos.col + 1) 
        #SE
        pos.setterValues(self.position.row + 1, self.position.col + 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row + 1, pos.col + 1)  
        #SO
        pos.setterValues(self.position.row + 1, self.position.col - 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row + 1, pos.col - 1)  
        return mat

class Knight(Piece):
    """
    Classe 'Bishop', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'N'                 #Imprime o 'Cavalo' como um 'N' 
        return '\u2658'             #Imprime o unicode do 'Cavalo'

    def canMove(self, pos):
        p = self.board.piece(pos)
        return (p == None) or p.color != self.color
    
    def possibleMoves(self):
        mat = CreateMatrix(self.board.row, self.board.col, None)
        pos = Position(0,0)
        
        pos.setterValues(self.position.row - 1, self.position.col - 2) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row - 2, self.position.col - 1) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row - 2, self.position.col + 1) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row - 1, self.position.col + 2) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row + 1, self.position.col + 2) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row + 2, self.position.col - 1) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row + 2, self.position.col - 1) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        pos.setterValues(self.position.row + 1, self.position.col - 2) #
        if self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
        return mat

class Queen(Piece):
    """
    Classe 'Queen', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'Q'                 #Imprime a 'Dama' como um 'Q' 
        return '\u2655'             #Imprime o unicode do 'Dama'

    def canMove(self, pos):
        p = self.board.piece(pos)
        return (p == None) or p.color != self.color
    def possibleMoves(self):
        """
        Cria uma Matriz de possíveis movimentos da 'Torre'.
        \nRetorno:
        \n- Matriz contendo os possíveis movimentos.
        """
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
        #NO
        pos.setterValues(self.position.row - 1, self.position.col - 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row - 1, pos.col -1)
        #NE
        pos.setterValues(self.position.row - 1, self.position.col + 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row - 1, pos.col + 1) 
        #SE
        pos.setterValues(self.position.row + 1, self.position.col + 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row + 1, pos.col + 1)  
        #SO
        pos.setterValues(self.position.row + 1, self.position.col - 1)
        while self.board.validPosition(pos) and self.canMove(pos):
            mat[pos.row][pos.col] = True
            if self.board.piece(pos) is not None and self.board.piece(pos).color is not self.color:
                break
            pos.setterValues(pos.row + 1, pos.col - 1)  
        return mat

class Pawn(Piece):
    """
    Classe 'Queen', contendo as informação da peça. Essa clase herda as informação da classe mãe 'Piece'.
    \nMétodos:
    \n- __str__:
    \n- canMove(self, pos):
    \n- possibleMoves(self):
    """
    def __str__(self):
        #return 'P'                 #Imprime a 'peão' como um 'P' 
        return '\u2659'             #Imprime o unicode do 'Peão'
    
    def thereIsOpponent(self, pos):
        p = self.board.piece(pos)
        if p == None:
            return False
        return p != None or p.color != self.color

    def free(self, pos):
        return self.board.piece(pos) == None

    def possibleMoves(self):
        mat = CreateMatrix(self.board.row, self.board.col, None)
        pos = Position(0,0)

        if self.color == Color.WHITE:
            pos.setterValues(self.position.row - 1, self.position.col) #
            if self.board.validPosition(pos) and self.free(pos):
                mat[pos.row][pos.col] = True   
            pos.setterValues(self.position.row - 2, self.position.col) #
            if self.board.validPosition(pos) and self.free(pos) and self.move_count == 0:
                mat[pos.row][pos.col] = True 
            pos.setterValues(self.position.row - 1, self.position.col - 1) #
            if self.board.validPosition(pos) and self.thereIsOpponent(pos):
                mat[pos.row][pos.col] = True
            pos.setterValues(self.position.row - 1, self.position.col + 1) #
            if self.board.validPosition(pos) and self.thereIsOpponent(pos):
                mat[pos.row][pos.col] = True  
        else:
            pos.setterValues(self.position.row + 1, self.position.col) #
            if self.board.validPosition(pos) and self.free(pos):
                mat[pos.row][pos.col] = True   
            pos.setterValues(self.position.row + 2, self.position.col) #
            if self.board.validPosition(pos) and self.free(pos) and self.move_count == 0:
                mat[pos.row][pos.col] = True 
            pos.setterValues(self.position.row + 1, self.position.col - 1) #
            if self.board.validPosition(pos) and self.thereIsOpponent(pos):
                mat[pos.row][pos.col] = True
            pos.setterValues(self.position.row + 1, self.position.col + 1) #
            if self.board.validPosition(pos) and self.thereIsOpponent(pos):
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

        self._allPieces = set()
        self._piecesCacth = set()

        self._check = False
        self.putPiecesInit()
    
    @property
    def check(self):
        return self._check
    @check.setter
    def check(self, check):
        self._check = check

    @property
    def shift(self):
        return self._shift

    @property
    def currentPlayer(self):
        return self._currentPlayer

    @property
    def finish(self):
        return self._finish
    @finish.setter
    def finish(self, finish):
        self._finish = finish

    @property
    def board(self):
        return self._board  
    @board.setter 
    def board(self,board):
        self._board = board    

    def getPiecesCacth(self, color): #PecasCapituradas
        aux = set()
        for x in self._piecesCacth:
            if x.color == color:
                aux.add(x)
        return aux

    def piecesInGame(self, color): #pecas em jogo
        aux = set()
        for x in self._allPieces:
            if x.color == color:
                aux.add(x)
        return aux.difference(self.getPiecesCacth(color))

    def opponent(self, color):
        if color == Color.BLACK:
            return Color.WHITE
        else:
            return Color.BLACK

    def getKing(self, color):
        for x in self.piecesInGame(color):
            if x.__class__ is King:
                return x
        return None    

    def thereIsCheck(self, color):    #Verifica se o rei dessa cor está em check
        R = self.getKing(color)
        if R == None:
            raise BoardException(f"Não tem Rei da cor {color} no tabuleiro")
        
        for x in self.piecesInGame(self.opponent(color)): #Para cada peça em game na cor oposta
            mat = x.possibleMoves()
            if mat[R.position.row][R.position.col]:
                return True
        return False

    def checkCheckMate(self, color):
        if not self.thereIsCheck(color):
            return False
        for x in self.piecesInGame(color):
            mat = x.possibleMoves()
            for i in range(self.board.row):
                for j in range(self.board.col):
                    if mat[i][j]:
                        posOrigin = x.position
                        posDestiny = Position(i,j)
                        p_catch = self.makeMove(posOrigin, posDestiny)
                        checkCheck = self.thereIsCheck(color)
                        self.resetMove(posOrigin,posDestiny, p_catch)
                        if not checkCheck:
                            return False
        return True

    def putNewPiece(self, col, row, piece):
        self.board.putPiece(piece,ChessPositon(col,row).toPosition()) #OK
        self._allPieces.add(piece) #OK

    def putPiecesInit(self):

        self.putNewPiece('a',1, Rook(self.board,Color.WHITE))
        self.putNewPiece('b',1, Knight(self.board, Color.WHITE))
        self.putNewPiece('c',1, Bishop(self.board, Color.WHITE))
        self.putNewPiece('d',1, Queen(self.board, Color.WHITE))
        self.putNewPiece('e',1, King(self.board, Color.WHITE))
        self.putNewPiece('f',1, Bishop(self.board, Color.WHITE))
        self.putNewPiece('h',1, Rook(self.board,Color.WHITE))
        self.putNewPiece('g',1, Knight(self.board, Color.WHITE))

        self.putNewPiece('a',8, Rook(self.board,Color.BLACK))
        self.putNewPiece('b',8, Knight(self.board, Color.BLACK))
        self.putNewPiece('c',8, Bishop(self.board, Color.BLACK))
        self.putNewPiece('e',8, Queen(self.board, Color.BLACK))
        self.putNewPiece('d',8, King(self.board, Color.BLACK))
        self.putNewPiece('f',8, Bishop(self.board, Color.BLACK))
        self.putNewPiece('h',8, Rook(self.board,Color.BLACK))
        self.putNewPiece('g',8, Knight(self.board, Color.BLACK))   

        self.putNewPiece('a',2, Pawn(self.board, Color.WHITE)) 
        self.putNewPiece('b',2, Pawn(self.board, Color.WHITE))
        self.putNewPiece('c',2, Pawn(self.board, Color.WHITE)) 
        self.putNewPiece('d',2, Pawn(self.board, Color.WHITE)) 
        self.putNewPiece('e',2, Pawn(self.board, Color.WHITE)) 
        self.putNewPiece('f',2, Pawn(self.board, Color.WHITE))
        self.putNewPiece('g',2, Pawn(self.board, Color.WHITE)) 
        self.putNewPiece('h',2, Pawn(self.board, Color.WHITE)) 
        
        self.putNewPiece('a',7, Pawn(self.board, Color.BLACK)) 
        self.putNewPiece('b',7, Pawn(self.board, Color.BLACK))
        self.putNewPiece('c',7, Pawn(self.board, Color.BLACK)) 
        self.putNewPiece('d',7, Pawn(self.board, Color.BLACK)) 
        self.putNewPiece('e',7, Pawn(self.board, Color.BLACK)) 
        self.putNewPiece('f',7, Pawn(self.board, Color.BLACK))
        self.putNewPiece('g',7, Pawn(self.board, Color.BLACK)) 
        self.putNewPiece('h',7, Pawn(self.board, Color.BLACK))     

        
        

    def makeAMove(self,origin, destiny):                #Realizar jogada
        pieceCatch = self.makeMove(origin, destiny)
        if self.thereIsCheck(self.currentPlayer):
            self.resetMove(origin, destiny, pieceCatch)
            raise BoardException("Você não pode se colocar em xeque!")
        
        if self.thereIsCheck(self.opponent(self.currentPlayer)):
            self.check = True
        else:
            self.check = False

        if self.checkCheckMate(self.opponent(self.currentPlayer)):
            self.finish = True
        else:
            self._shift += 1
            self.changePlayer()

    def resetMove(self, origin, destiny, pieceCatch):
        p = self.board.removePiece(destiny)
        p.decrementMovement()

        if pieceCatch != None:
            self.board.putPiece(pieceCatch, destiny)
            self._piecesCacth.remove(pieceCatch)
        self.board.putPiece(p,origin)

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

    def makeMove(self, origin, destiny):        #executa movimento
        p = self.board.removePiece(origin)     #Remove a peça da origem e salva em 'p'
        p.increaseMovement()                    #Acrescenta o movimento da peça 'p'

        p_catch = self.board.removePiece(destiny)  #Remove a peça do destino e salva em p_catch
        self.board.putPiece(p,destiny)             #Coloca a pela da origem no destino

        if p_catch != None:
            self._piecesCacth.add(p_catch)

        return p_catch

    

