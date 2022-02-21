def rLSE(matrices):
    M = len(matrices['AtA'])
    N = len(matrices['A'])
    w = []
    tmp = [[0 for i in range(N)] for j in range(M)]
    for r in range(M):
        for c in range(N):
            sum = 0
            for k in range(M):
                sum += matrices['invAtA'][r][k] * matrices['A'][c][k]
            tmp[r][c] = sum
    for r in range(M):
        sum = 0
        for k in range(N):
            sum += tmp[r][k] * matrices['b'][k]
        w.append(sum)
    return w