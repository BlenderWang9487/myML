def CholeskyDecomposition(m):
    M = len(m)
    lower_triangle = [[0 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(i+1):
            if i == j:
                lower_triangle[i][j] = pow(
                    m[i][j] -
                    sum([lower_triangle[j][k] * lower_triangle[j][k] for k in range(j-1)]),
                    0.5
                )
            else:
                lower_triangle[i][j] = (
                    m[i][j] -
                    sum([lower_triangle[j][k] * lower_triangle[i][k] for k in range(j-1)])
                ) / lower_triangle[j][j]
    return lower_triangle