from myML import *

if __name__ == "__main__":
    input_data = InputFileParser("./data/test.txt")
    print(input_data)
    matrices = MatrixConstruct(input_data,M=2,lamb=0)
    CholeskyDecomposition(matrices)
    InverseCalculate(matrices)
    print(matrices)
