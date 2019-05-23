#Aplicativo que consome as bibliotecas do jogo e comunica com usuário

class Screen:

    @staticmethod
    def PrintBoard(board):
        for r in range(board.row):
            for c in range(board.col):
                if (board.piece(r,c) == None):
                    print('- ',end='')
                else:
                    print(f'{board.piece(r,c)} ',end='')
            print()