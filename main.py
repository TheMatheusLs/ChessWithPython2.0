from BoardModule import *  #Importa os modulos do tabuleiro
from ApplicationModule import *            #Importa o modulo de tela
from GameModule import *                        #Importa os modulos do jogo

try:
    tab = Board(8,8)        #Cria um tabuleiro 8x8

    tab.putPiece(Tower(tab,Color.BRANCA),Position(0,0))  #Colaca uma torre preta no tabuleio na posição x= 0 e y= 0
    tab.putPiece(Tower(tab,Color.PRETA),Position(1,5))  #Colaca uma torre preta no tabuleio na posição x= 1 e y= 3
    tab.putPiece(King(tab,Color.PRETA),Position(0,2))   #Colaca um rei preto no tabuleio na posição x= 2 e y= 4
    tab.putPiece(Tower(tab,Color.BRANCA),Position(3,7))
    tab.putPiece(King(tab,Color.PRETA),Position(2,7))
    
    Screen.PrintBoard(tab)      #Imprime o tabuleiro 'tab'
except BoardException as e:
    print(e)