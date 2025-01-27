import numpy as np

a=np.arange(1,51)
a=a.reshape(10,5)
print(a)

print(a[0])
print(a[3])
# (row,column)
print(a[2,4])
print(a[2:5])
print(a[:,2])
print(a[2:5,2])