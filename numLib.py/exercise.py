import numpy as np

# Create a numpy array of size 10, filled with zeros.

a=np.zeros(10)
print(a)


# Create a numpy array with values ranging from 10 to 49
b=np.arange(10,49)
print(b)

#Create a numpy matrix of 2*2 integers, filled with ones
c=np.ones([2,2],dtype=np.int8)
print(c)

#Create a numpy matrix of 3*2 float numbers, filled with ones.
d= np.ones([3,2],dtype=np.float16)
print(d)

#Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
X = np.arange(4, dtype=np.int8)

print(np.ones_like(X))

#Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.
X = np.arange(4, dtype=np.int8)

print(np.zeros_like(X))