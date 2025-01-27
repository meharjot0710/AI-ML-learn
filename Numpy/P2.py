# importing numpy
import numpy as np

# np.empty((rows,columns),dtype) creates an empty array of random data
a=np.empty((4,4),dtype=int)
print(a)

# np.ones((rows,columns),dtype) creates an array of ones
b=np.ones((3,5))
print(b)
c=np.ones((3,5),dtype=str)
print(c)
d=np.ones((3,5),dtype=bool)
print(d)


# np.zeros((rows,columns),dtype) creates an array of ones
e=np.zeros((3,5))
print(e)
f=np.zeros((3,5),dtype=str)
print(f)
g=np.zeros((3,5),dtype=bool)
print(g)