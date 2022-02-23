from . import MatrixConstruct,InverseCalculate,MatrixMultiply,MatrixMultiScalar
from myML.LUDecomposition import LUDecomposition

def NewtonMethod(input_data,M=2,x=[]):
    m = MatrixConstruct(input_data,M,0)
    
    if len(x) == 0:
        x = [[0] for i in range(M)]
    
    _2AtA = MatrixMultiScalar(m['AtA'],2)
    L,U = LUDecomposition(_2AtA)
    inv_2AtA = InverseCalculate(L,U)
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
    