#Aplicativo que consome as bibliotecas do jogo e comunica com usuário
from BoardModule import Position

class Screen:                                               #Classe para a tela

    @staticmethod                                           #Método Static
    def PrintBoard(board):                                  #Método para imprimir um tabuleiro
        for r in range(board.row):                          
            for c in range(board.col):
                if (board.piece(Position(r,c)) == None):
                    print('- ',end='')
                else:
                    print(f'{board.piece(Position(r,c))} ',end='')
            print()