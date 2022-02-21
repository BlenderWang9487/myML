from myML import *

if __name__ == "__main__":
    M = 3
    input_data = InputFileParser("./data/test.txt")
    matrices = MatrixConstruct(input_data,M,0)
    CholeskyDecomposition(matrices)
    InverseCalculate(matrices)
    w_vector = rLSE(matrices)
    print(w_vector)
    tmp = [[0 for i in range(M)] for j in range(M)]
    for r in range(M):
        for c in range(M):
            sum = 0
            for k in range(M):
                sum += matrices['invAtA'][r][k] * matrices['AtA'][k][c]
            tmp[r][c] = sum
    print(tmp)