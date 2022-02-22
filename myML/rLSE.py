from . import CholeskyDecomposition, MatrixConstruct, MatrixMultiply, InverseCalculate
def rLSE(input_data,M=2,lamb=1):
    matrices = MatrixConstruct(input_data,M,lamb)

    lower_traingle = CholeskyDecomposition(matrices['AtA_lambdaI'])
    inv_lower = InverseCalculate(lower_traingle)
    inv_AtA_lambdaI = MatrixMultiply(inv_lower,inv_lower,[True,False])
    inv_AtA_lambdaI_At = MatrixMultiply(inv_AtA_lambdaI,matrices['A'],[False,True])
    x = MatrixMultiply(inv_AtA_lambdaI_At,matrices['b'])

    err = 0
    Ax = MatrixMultiply(matrices['A'],x)
    for i in range(len(input_data)):
        err += (Ax[i][0] - matrices['b'][i][0])**2
    
    return x, err