from . import MatrixConstruct,CholeskyDecomposition,InverseCalculate,MatrixMultiply,MatrixMultiScalar

def NewtonMethod(input_data,M=2):
    m = MatrixConstruct(input_data,M,0)
    
    x = [[0] for i in range(M)]
    _2AtA = MatrixMultiScalar(m['AtA'],2)
    lower_triangle = CholeskyDecomposition(_2AtA)
    inv_lower = InverseCalculate(lower_triangle)
    inv_2AtA = MatrixMultiply(inv_lower,inv_lower,[True,False])
    _2AtAx = MatrixMultiply(_2AtA,x)
    _2Atb = MatrixMultiply(MatrixMultiScalar(m['A'],2),m['b'],[True,False])
    tmp_sub = []
    for i in range(M):
        tmp_sub.append([_2AtAx[i][0]-_2Atb[i][0]])
    neg_x = MatrixMultiply(inv_2AtA,tmp_sub)
    x1 = []
    for i in range(M):
        x1.append([x[i][0] - neg_x[i][0]])

    err = 0
    Ax = MatrixMultiply(m['A'],x1)
    for i in range(len(input_data)):
        err += (Ax[i][0] - m['b'][i][0])**2
    
    return x1, err
    