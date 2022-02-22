from myML import rLSE, MatrixMultiply, InputFileParser
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    M = 3
    lamb = 10000
    input_data = InputFileParser("./data/test.txt")
    
    min_lamb = 0
    pre_err = 9999999999999999
    for i in range(lamb):
        matrices, err = rLSE(input_data,M,i)
        if err < pre_err:
            min_lamb = i
            pre_err = err
    matrices, err = rLSE(input_data,M,min_lamb)
    print("lambda is:\n",min_lamb,"\nx vector is:\n",matrices['x'],"Total Err is: ",err,"\n")

    x = np.array([p[0] for p in input_data])
    y = np.array([p[1] for p in input_data])
    fig, ax = plt.subplots()

    x_for_line = np.linspace(min(x),max(x),1000)
    y_for_line = 0
    for i in range(M):
        y_for_line += x_for_line**(M-i-1)*matrices['x'][i][0]
    
    ax.scatter(x,y)
    ax.plot(x_for_line,y_for_line)

    plt.savefig('./data/fig.png')

    """ll = MatrixMultiply(matrices['L'],matrices['L'],[False,True])
    max_diff = 0
    diff_list = []
    for i in range(M):
        for j in range(M):
            diff = abs(ll[i][j] - matrices['AtA'][i][j])
            max_diff = max(max_diff, diff)
            diff_list.append(diff)
    print("max difference between LL and AtA: \n",max_diff," in:",diff_list)
    print(matrices['AtA'])"""