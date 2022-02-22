from . import CholeskyDecomposition, MatrixConstruct, MatrixMultiply, InverseCalculate
def rLSE(input_data,M=2,lamb=1):
    matrices = MatrixConstruct(input_data,M,lamb)
    CholeskyDecomposition(matrices)
    InverseCalculate(matrices)
    AtA_I_At = MatrixMultiply(matrices['invAtA'],matrices['A'],[False,True])
    matrices['x'] = MatrixMultiply(AtA_I_At,matrices['b'])
    err = 0
    Ax = MatrixMultiply(matrices['A'],matrices['x'])
    for i in range(len(input_data)):
        err += (Ax[i][0] - matrices['b'][i][0])**2
    return matrices, err