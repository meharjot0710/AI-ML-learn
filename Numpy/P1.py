# Importing numpy
import numpy as np

# List
l=[1,2,3,4,5,6]
print(l)

# 1D array
a=np.array([1,2,3,4,5,6])
print(a)

# 2D array
b=np.array([[1,2,3],
            [4,5,6]])
print(b)

# 3D array
c=np.array([[1,2],
            [3,4],
            [5,6]])
print(c)

# type(a) tells the data type of variable a
# a.size tells the number of elements in a
# a.shape tells the shape of the array in the form of (rows,columns)
# a.dtype tells the datatype of the elements present in the array


print(type(a),a.size,a.shape,a.dtype)
print(type(b),b.size,b.shape,b.dtype)
print(type(c),c.size,c.shape,c.dtype)


# Note:- The numpy array can only have elements with the same datatype

# The c.transpose function transposes the matrix i.e. it replaces the rows with columns and columns with rows

print(c.transpose())