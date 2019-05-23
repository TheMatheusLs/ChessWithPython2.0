def CreateMatrix(nrow, ncol, element):
    matrix = []
    for r in range(nrow):
        #Cria a linha i
        row = []    #Lista vazia
        for c in range(ncol):
            row.append(element)
        matrix.append(row)
    return matrix