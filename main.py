from BoardModule import Position, Board, Color  #Importa os modulos do tabuleiro
from ApplicationModule import Screen            #Importa o modulo de tela
from GameModule import *                        #Importa os modulos do jogo

tab = Board(8,8)        #Cria um tabuleiro 8x8

tab.putPiece(Tower(tab,Color.preta),Position(0,0))  #Colaca uma torre preta no tabuleio na posição x= 0 e y= 0
tab.putPiece(Tower(tab,Color.preta),Position(1,3))  #Colaca uma torre preta no tabuleio na posição x= 1 e y= 3
tab.putPiece(King(tab,Color.preta),Position(2,4))   #Colaca um rei preto no tabuleio na posição x= 2 e y= 4

Screen.PrintBoard(tab)      #Imprime o tabuleiro 'tab'