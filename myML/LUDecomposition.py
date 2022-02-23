from . import MatrixPrint
import copy
def LUDecomposition(m):
    M = len(m)
    L = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    U = copy.deepcopy(m)
    for c in range(M):
        for r in range(c+1,M):
            L[r][c] = U[r][c] / U[c][c]
            for k in range(M):
                if k == c:
                    U[r][k] = 0
                else:
                    U[r][k] -= U[c][k] * L[r][c]
    return L,U