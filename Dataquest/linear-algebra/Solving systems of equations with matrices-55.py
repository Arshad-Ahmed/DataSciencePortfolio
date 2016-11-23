## 2. Systems of equations as matrices ##

import numpy as np

# Set the dtype to float to do float math with the numbers.
matrix = np.asarray([
    [2, 1, 25],
    [3, 2, 40]  
], dtype=np.float32)

matrix[0] *= 2

# Subtract the second row from the first row.
matrix[0] -= matrix[1]

# Subtract three times the first row from the second row.
matrix[1] -= (3 * matrix[0])

# Divide the second row by two.
matrix[1] /= 2

## 4. Solving more complex equations ##

import numpy as np

matrix = np.asarray([
    [1, 2, 0, 7],
    [0, 3, 3, 11],
    [1, 2, 2, 11]
], dtype=np.float32)

matrix[2] -= matrix[0]

# Divide the third row by 2.
matrix[2] /= 2

# Subtract three times the third row from the second row
matrix[1] -= (matrix[2] * 3)

# Divide the second row by three
matrix[1] /= 3

# Subtract two times the second row from the first row
matrix[0] -= (2 * matrix[1])

## 5. Echelon form ##

matrix = np.asarray([
    [0, 0, 0, 7],
    [0, 0, 1, 11],
    [1, 2, 2, 11],
    [0, 5, 5, 1]
], dtype=np.float32)

matrix[[0,2]]=matrix[[2,0]]
matrix[[2,3]]=matrix[[3,2]]

matrix[[1,2]] = matrix[[2,1]]
