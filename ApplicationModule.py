#Aplicativo que consome as bibliotecas do jogo e comunica com usuário
from BoardModule import *
from GameModule import *
import socket      
import os           #Módulo do sistema

os.system('echo on')

class Screen:                                               #Classe para a tela
    COLOR_RED = '\033[1;31m'    #Código para a cor vermelha
    COLOR_YELLOW = '\033[33m'   #Código para a cor amarela
    COLOR_RESET = '\033[m'      #Código para voltar a cor normal do terminal
    BACKGROUND = '\033[46m'     #Backgound azul

    @staticmethod
    def printGame(game):            #Imprimir partida
        Screen.PrintBoard(game.board)      #Imprime o tabuleiro 'tab'
        print()
        Screen.printPiecesCatch(game)
        print(f'\nCurrent Shift: {game.shift}')
        if not game.finish:
            print(f'Waiting for the {str(game.currentPlayer).replace("Color.","").capitalize()} play') 
            if game.check:
                print(f'{Screen.COLOR_RED}CHECK!{Screen.COLOR_RESET}')
        else:
            print(f'{Screen.COLOR_RED}CHECKMATE!{Screen.COLOR_RESET}')
            print(f'Winner: {str(game.currentPlayer).replace("Color.","").capitalize()}')
    @staticmethod
    def printPiecesCatch(game):         #Imprimir peças capturadas
        print('Catch pieces: ')
        print('White: ',end='')
        Screen.printSet(game.getPiecesCacth(Color.WHITE))
        print(f'Black: {Screen.COLOR_YELLOW}',end='')
        Screen.printSet(game.getPiecesCacth(Color.BLACK))
        print(f'{Screen.COLOR_RESET}',end='')

    @staticmethod
    def printSet(vSet):         #Imprimir conjunto
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

        
        for r in range(board.row):     
            print(f'{8-r} ',end='')                     
            for c in range(board.col):
                if (possiblePosition[r][c]):
                    print(f'{Screen.BACKGROUND}',end='')
                else:
                    print(f'{Screen.COLOR_RESET}',end='')
                Screen.printPiece(board.piece(Position(r,c)))
            print(Screen.COLOR_RESET)
        print('  a b c d e f g h')

    @staticmethod
    def printPiece(piece):
        if piece == None:
            print('- ',end='')
        else:
            if (piece.color == Color.WHITE):
                print(piece,end=' ')
            else:
                print(f'{Screen.COLOR_YELLOW}',end='') #Código da cor
                print(piece,end=' ')
                print(f'{Screen.COLOR_RESET}',end='') #Código para limpar a cor

    @staticmethod
    def getPositionChess():
        s = input()
        if len(s) == 2 and s[0] in 'abcdefgh' and s[1] in '12345678':
            col = s[0]
            row = int(s[1])
            return ChessPositon(col, row)
        raise BoardException("Comando inválido!")


