import numpy as np
import matplotlib.pyplot as plt


#create checkered grid based on position in array
def chessboard():
    rows=8
    cols=8
    chess=np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            chess[i,j]=i+j
            if np.any(chess[i,j]%2==0):
                chess[i,j]=0
            else:
                chess[i,j]=1
    return chess

if __name__ == '__main__':
    chess = chessboard()
    plt.imshow(chess)
    plt.colorbar()
    plt.show()
    print (chess)
