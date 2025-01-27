import numpy as np

a=np.arange(0,18).reshape((6,3))
b=np.arange(20,38).reshape((6,3))
print(a)
print(b)

print(a+b)
print(np.add(a,b))
print(a-b)
print(np.subtract(a,b))
print(a*b)
print(np.multiply(a,b))
print(a/b)
print(np.divide(a,b))

# To multiply the matrices, a@b is used
b=b.reshape(3,6)
print(a@b)
print(a.dot(b))

print(b.max())
print(b.min())
print(b.argmin())
print(b.argmin())

print(np.sum(b))

# axis = 1 means row & axis = 0 means column
print(np.sum(b,axis=1))
print(np.sum(b,axis=0))

print(np.mean(a))
print(np.mean(b))
print(np.sqrt(a))
print(np.sqrt(b))
print(np.std(a))
print(np.std(b))
print(np.log(a))
print(np.log(b))