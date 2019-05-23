#Inteligência do jogo de xadrez, como as peças vão se movimentação. Mecanica do jogo
from BoardModule import Piece       #Importa o módulo das peças

class Tower(Piece):                 #Classe com as regras da 'torre' e herda da classe Peça
    
    def __str__(self):
        return 'T'                  #Imprime a 'Torre' como um 'T'    
    
class King(Piece):                  #Classe com as regras da 'rei' e herda da classe Peça
    
    def __str__(self):
        return 'K'                  #Imprime a 'Rei' como um 'R' 