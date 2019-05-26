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

            Screen.printGame(game)
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
            print(f'{Screen.COLOR_RED}{Screen.WARNING} {e} {Screen.WARNING}{Screen.COLOR_RESET}')
            input()

    os.system('cls')                    #Limpa a tela
    Screen.printGame(game)              #Imprime a partida

except BoardException as e:             #Trata o erro
    print(f'{Screen.COLORa1_RED}{Screen.WARNING} {e} {Screen.WARNING}{Screen.COLOR_RESET}')       #Imprime o erro para na tela