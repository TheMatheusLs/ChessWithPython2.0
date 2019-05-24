#Aplicativo que consome as bibliotecas do jogo e comunica com usuário
from BoardModule import *
from GameModule import *
import socket      
import os           #Módulo do sistema

os.system('echo on')

class Screen:                                               #Classe para a tela

    @staticmethod
    def printGame(game):
        Screen.PrintBoard(game.board)      #Imprime o tabuleiro 'tab'
        print()
        Screen.printPiecesCatch(game)
        print(f'\nCurrent Shift: {game.shift}')
        print(f'Waiting for the {str(game.currentPlayer).replace("Color.","").capitalize()} play') 

    @staticmethod
    def printPiecesCatch(game):
        print('Catch pieces: ')
        print('White: ',end='')
        Screen.printSet(game.getPiecesCacth(Color.WHITE))
        print('Black: \033[33m',end='')
        Screen.printSet(game.getPiecesCacth(Color.BLACK))
        print('\033[m',end='')

    @staticmethod
    def printSet(vSet):
        print('[',end='')
        for x in vSet:
            print(f'{x} ',end='')
        print(']')

    @staticmethod                                           #Método Static
    def PrintBoard(board):                                  #Método para imprimir um tabuleiro
        for r in range(board.row):     
            print(f'{8-r} ',end='')                     
            for c in range(board.col):
                Screen.printPiece(board.piece(Position(r,c)))
            print()
        print('  a b c d e f g h')
    
    @staticmethod                                           #Método Static
    def PrintBoardAssist(board, possiblePosition):                                  #Método para imprimir um tabuleiro

        BACKGROUND = '\033[46m'  
        RESETBACKGROUND = '\033[m'
        for r in range(board.row):     
            print(f'{8-r} ',end='')                     
            for c in range(board.col):
                if (possiblePosition[r][c]):
                    print(BACKGROUND,end='')
                else:
                    print(RESETBACKGROUND,end='')
                Screen.printPiece(board.piece(Position(r,c)))
            print(RESETBACKGROUND)
        print('  a b c d e f g h')

    @staticmethod
    def printPiece(piece):
        if piece == None:
            print('- ',end='')
        else:
            if (piece.color == Color.WHITE):
                print(piece,end=' ')
            else:
                print('\033[33m',end='') #Código da cor
                print(piece,end=' ')
                print('\033[m',end='') #Código para limpar a cor

    @staticmethod
    def getPositionChess():
        s = input()
        if len(s) == 2 and s[0] in 'abcdefgh':
            col = s[0]
            row = int(s[1])
            return ChessPositon(col, row)
        raise BoardException("Comando inválido!")


