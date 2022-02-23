from myML import rLSE, NewtonMethod, MatrixMultiply, InputFileParser
import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        M = int(sys.argv[1])
        lamb = float(sys.argv[2])
    else:
        M = 3
        lamb = 0
    input_data = InputFileParser("./data/test.txt")
    
    x_rLSE, err = rLSE(input_data,M,lamb)
    print("rLSE====> f(x) is:")
    text = ""
    for i in range(M-1):
        text += str(x_rLSE[i][0]) + "*X^" + str(M-i-1) + " "
        if i != M-1 and x_rLSE[i+1][0] >= 0:
            text += "+ "
    text += str(x_rLSE[-1][0])
    print(text,"\nTotal Err is: ",err,"\n")

    # initial_x = [[3.023],[4.906],[-0.231]]
    x_Newton, err2 = NewtonMethod(input_data,M)
    """for i in range(2):
        x_Newton, err2 = NewtonMethod(input_data,M,x_Newton)"""
    print("Newton==> f(x) is:")
    text = ""
    for i in range(M-1):
        text += str(x_Newton[i][0]) + "*X^" + str(M-i-1) + " "
        if i != M-1 and x_Newton[i+1][0] >= 0:
                text += "+ "
    text += str(x_Newton[-1][0])
    print(text,"\nTotal Err is: ",err2,"\n")

    x = np.array([p[0] for p in input_data])
    y = np.array([p[1] for p in input_data])
    axs = (plt.figure(constrained_layout=True)
       .subplots(2, 1, sharex=True, sharey=True))

    x_for_line = np.linspace(min(x),max(x),1000)
    y_for_line_rLSE = 0
    y_for_line_Newton = 0
    for i in range(M):
        y_for_line_rLSE += x_for_line**(M-i-1) * x_rLSE[i][0]
        y_for_line_Newton += x_for_line**(M-i-1) * x_Newton[i][0]
        
    
    axs[0].scatter(x,y)
    axs[0].plot(x_for_line,y_for_line_rLSE)
    axs[0].title.set_text('rLSE')

    axs[1].scatter(x,y)
    axs[1].plot(x_for_line,y_for_line_Newton)
    axs[1].title.set_text('Newton')

    plt.savefig('./data/fig.png')