from .MatrixConstruct import MatrixMultiply,MatrixPrint
import copy

def LowerInverseCalculate(L):
    M = len(L)
    inv = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1,M):
            for k in range(M):
                inv[j][k] -= inv[i][k]  / L[i][i] * L[j][i]
    for i in range(M):
        for j in range(i+1):
            inv[i][j] /= L[i][i]
    return inv

def InverseCalculate(L,U):
    M = len(L)
    invL = copy.deepcopy(L)
    invU = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(M):
            if i > j:
                invL[i][j] *= -1
    for c in range(M-1,-1,-1):
        for r in range(c-1,-1,-1):
            for k in range(M):
                invU[r][k] -= invU[c][k] / U[c][c] * U[r][c]
    for r in range(M):
        for c in range(r,M):
            invU[r][c] /= U[r][r]
    return MatrixMultiply(invU,invL)