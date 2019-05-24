from BoardModule import *  #Importa os modulos do tabuleiro
from ApplicationModule import *            #Importa o modulo de tela
from GameModule import *                        #Importa os modulos do jogo
import socket      
import os           #Módulo do sistema

try:
       
    game = ChessGame()

    while not game.finish:
        os.system('cls')
        Screen.PrintBoard(game.board)      #Imprime o tabuleiro 'tab'

        print('\nOrigem: ')
        origin = Screen.getPositionChess().toPosition()

        possiblePosition = game.board.piece(origin).possibleMoves()

        os.system('cls')
        Screen.PrintBoardAssist(game.board, possiblePosition)      #Imprime o tabuleiro 'tab'

        print('\nDestino: ')
        destiny = Screen.getPositionChess().toPosition()

        game.makeMove(origin, destiny)

except BoardException as e:
    print(e)