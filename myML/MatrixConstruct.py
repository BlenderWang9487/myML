from numpy import matrix


def MatrixConstruct(points,M=2,lamb=1):
    matrices = {}
    matrices['b'] = []
    matrices['A'] = []
    for point in points:
        matrices['b'].append(point[1])
        matrices['A'].append([point[0]**(M-i-1) for i in range(M)])
    matrices['AtA'] = [[0 for i in range(M)] for j in range(M)]
    for r in range(M):
        for c in range(M):
            sum = 0
            for k in range(len(points)):
                sum += matrices['A'][k][r] * matrices['A'][k][c]
            matrices['AtA'][r][c] = sum
    return matrices