from BoardModule import Position, Board, Color, BoardException  #Importa os modulos do tabuleiro
from ApplicationModule import Screen            #Importa o modulo de tela
from GameModule import *                        #Importa os modulos do jogo

try:
    tab = Board(8,8)        #Cria um tabuleiro 8x8

    tab.putPiece(Tower(tab,Color.preta),Position(0,0))  #Colaca uma torre preta no tabuleio na posição x= 0 e y= 0
    tab.putPiece(Tower(tab,Color.preta),Position(1,9))  #Colaca uma torre preta no tabuleio na posição x= 1 e y= 3
    tab.putPiece(King(tab,Color.preta),Position(0,2))   #Colaca um rei preto no tabuleio na posição x= 2 e y= 4

    Screen.PrintBoard(tab)      #Imprime o tabuleiro 'tab'
except BoardException as e:
    print(e)