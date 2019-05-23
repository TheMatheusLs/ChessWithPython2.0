
def CreateMatrix(nrow, ncol, element):  #Método para criar uma matriz de dimenção variável de elemento variável
    matrix = []                 #Cria uma lista vazia
    for r in range(nrow):       #For para varrer as linhas    
        row = []                #Lista de linha vazia
        for c in range(ncol):   #For para varrer as colunas
            row.append(element) #Adiciona o elemento a colunas
        matrix.append(row)      #Adiciona a linha a matriz
    return matrix               #Retorna a matriz