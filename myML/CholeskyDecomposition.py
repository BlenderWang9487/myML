def CholeskyDecomposition(matrices):
    M = len(matrices['AtA'])
    matrices['L'] = [[0 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1):
            if i == j:
                matrices['L'][i][j] = (
                    matrices['AtA'][i][j] - 
                    sum([matrices['L'][j][k]**2 for k in range(j-1)])
                )**(0.5)
            else:
                matrices['L'][i][j] = (
                    matrices['AtA'][i][j] -
                    sum([matrices['L'][j][k] * matrices['L'][i][k] for k in range(j-1)])
                )**(0.5) / matrices['L'][j][j]
    return