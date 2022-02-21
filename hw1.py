from myML import *

if __name__ == "__main__":
    input_data = InputFileParser("./data/test.txt")
    matrices = MatrixConstruct(input_data,M=3,lamb=0)
    CholeskyDecomposition(matrices)
    InverseCalculate(matrices)
    w_vector = rLSE(matrices)
    print(w_vector)
