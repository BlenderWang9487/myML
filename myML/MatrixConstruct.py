def MatrixConstruct(points,M,lamb):
    matrices = {}
    matrices['b'] = []
    matrices['A'] = []
    for point in points:
        matrices['b'].append([point[1]])
        matrices['A'].append([pow(point[0],(M-i-1)) for i in range(M)])
    matrices['AtA'] = MatrixMultiply(matrices['A'],matrices['A'],[True,False])
    matrices['AtA_lambdaI'] = MatrixMultiply(matrices['A'],matrices['A'],[True,False])
    for i in range(M):
        matrices['AtA_lambdaI'][i][i] += lamb
    return matrices

def MatrixMultiply(m1,m2,mode=[False,False]): # mode False,False both matrices aren't transposes, True,False first matrix is transpose ...
    R = (len(m1) if not mode[0] else len(m1[0]))
    C = (len(m2[0]) if not mode[1] else len(m2))
    K = (len(m1[0]) if not mode[0] else len(m1))
    result = [[0 for i in range(C)] for j in range(R)]
    for r in range(R):
        for c in range(C):
            sum = 0
            for k in range(K):
                sum += (m1[r][k] if not mode[0] else m1[k][r]) * (m2[k][c] if not mode[1] else m2[c][k])
            result[r][c] = sum
    return result

def MatrixMultiScalar(m,scalar):
    R = len(m)
    C = len(m[0])
    result = [[0 for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            result[r][c] = m[r][c] * scalar
    return result

def MatrixPrint(m):
    text = "["
    for r in m:
        text += "[\t"
        for c in r:
            text += str(c) + "\t"
        text += " ]\n"
    text += "]"
    print(text)
    return
    