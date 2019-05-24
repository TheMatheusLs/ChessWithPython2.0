#Aplicativo que consome as bibliotecas do jogo e comunica com usuário
from BoardModule import *
from GameModule import *
import socket      
import os           #Módulo do sistema

os.system('echo on')

class Screen:                                               #Classe para a tela

    @staticmethod                                           #Método Static
    def PrintBoard(board):                                  #Método para imprimir um tabuleiro
        for r in range(board.row):     
            print(f'{8-r} ',end='')                     
            for c in range(board.col):
                if (board.piece(Position(r,c)) == None):
                    print('- ',end='')
                else:
                    Screen.printPiece(board.piece(Position(r,c)))
                    print(' ',end='')
            print()
        print('  a b c d e f g h')
    
    @staticmethod
    def printPiece(piece):
        if (piece.color == Color.BRANCA):
            print(piece,end='')
        else:
            print('\033[0;33m',end='') #Código da cor
            print(piece,end='')
            print('\033[m',end='') #Código para limpar a cor

    @staticmethod
    def getPositionChess():
        s = input()
        col = s[0]
        row = int(s[1])
        return ChessPositon(col, row)


