from BoardModule import *  #Importa os modulos do tabuleiro
from ApplicationModule import *            #Importa o modulo de tela
from GameModule import *                        #Importa os modulos do jogo
import socket      
import os           #Módulo do sistema

try:
       
    game = ChessGame()

    while not game.finish:
        try:
            os.system('cls')                   #Limpa a tela
            Screen.PrintBoard(game.board)      #Imprime o tabuleiro 'tab'
            print(f'\nCurrent Shift: {game.shift}')
            print(f'Waiting for the {str(game.currentPlayer).replace("Color.","").capitalize()} play')                            


            print('\nOrigem: ')
            origin = Screen.getPositionChess().toPosition()
            game.validateOriginPosition(origin)

            possiblePosition = game.board.piece(origin).possibleMoves()

            os.system('cls')
            Screen.PrintBoardAssist(game.board, possiblePosition)      #Imprime o tabuleiro 'tab'

            print('\nDestino: ')
            destiny = Screen.getPositionChess().toPosition()
            game.validateOriginDestiny(origin, destiny)

            game.makeAMove(origin, destiny)
        except BoardException as e:
            e = str(e).replace("'","")
            print(f'\033[31m{e}\033[m')
            input()
except BoardException as e:
    print(f'\033[1;31m{e}\033[m')