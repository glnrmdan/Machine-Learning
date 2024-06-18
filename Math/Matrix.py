import numpy as np
from scipy.signal import convolve2d

# Define the 5x5 matrix
matrix1 = np.array([[7, 2, 3, 3, 8], 
                    [4, 5, 3, 8, 4],
                    [3, 3, 2, 8, 4],
                    [2, 8, 7, 2, 7],
                    [5, 4, 4, 5, 4]])

# Define the 3x3 matrix
matrix2 = np.array([[1, 0, -1], 
                    [1, 0, -1],
                    [1, 0, -1]])

# Perform matrix convolution
result = convolve2d(matrix1, matrix2, mode='valid')

# Print the result
print(result)