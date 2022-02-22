from .MatrixConstruct import MatrixMultiply

def InverseCalculate(matrices):
    M = len(matrices['AtA'])
    inv = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1,M):
            for k in range(M):
                inv[j][k] -= inv[i][k]  / matrices['L'][i][i] * matrices['L'][j][i]
    for i in range(M):
        for j in range(i+1):
            inv[i][j] /= matrices['L'][i][i]
    matrices['invL'] = inv
    matrices['invAtA'] = MatrixMultiply(inv,inv,[True,False])
    return