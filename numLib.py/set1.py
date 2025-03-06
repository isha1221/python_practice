##NOTE: In Python, lists work like arrays in other languages, but they are slower. You can use NumPy arrays for better performance

import sys
import numpy as np
A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

print(A[:, :2])

##Array type

a=np.array([1, 2, 3, 4])
a.dtype
#dtype('int64')
b=np.array([0. , 0.5, 1. , 1.5, 2. ])
b.dtype
#dtype('float64')
np.array([1, 2, 3, 4], dtype=np.float)
# array([1., 2., 3., 4.])
np.array([1, 2, 3, 4], dtype=np.int8)
# array([1, 2, 3, 4], dtype=int8)
c = np.array(['a', 'b', 'c'])
c.dtype
#dtype('<U1')
d = np.array([{'a': 1}, sys])
d.dtype
#dtype('O')




##Dimensions and shapes
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
A.shape
A.ndim
A.size

# Indexing and Slicing of Matrices
# Square matrix
A = np.array([
#.   0. 1. 2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
])

A[1][0] 
##row,column
A[1, 0]
A[0:2]
A[:, :2]
A[:2, :2]
A[:2, 2:]
A[1] = np.array([10, 10, 10])
A[2] = 99


##NOTE: whenever an array is modified it doesnot modify the original aarray a new array is created everytime 