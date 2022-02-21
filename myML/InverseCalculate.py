def InverseCalculate(matrices):
    M = len(matrices['AtA'])
    inv = [[0 if i != j else 1 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1,M):
            multi = -(matrices['L'][j][i] / matrices['L'][i][i])
            for k in range(M):
                inv[j][k] += inv[i][k] * multi
    for i in range(M):
        for j in range(M):
            inv[i][j] /= matrices['L'][i][i]
    invAtA = [[0 for i in range(M)] for j in range(M)]
    for r in range(M):
        for c in range(M):
            sum = 0
            for k in range(M):
                sum += inv[k][r] * inv[k][c]
            invAtA[r][c] = sum
    matrices['invAtA'] = invAtA
    return