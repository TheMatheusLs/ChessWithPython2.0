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