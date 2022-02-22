from .MatrixConstruct import MatrixMultiply

def InverseCalculate(lower_triangle):
    M = len(lower_triangle)
    inv = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1,M):
            for k in range(M):
                inv[j][k] -= inv[i][k]  / lower_triangle[i][i] * lower_triangle[j][i]
    for i in range(M):
        for j in range(i+1):
            inv[i][j] /= lower_triangle[i][i]
    return inv