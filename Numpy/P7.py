import numpy as np

print(np.random.random(2))
print(np.random.random((2,2)))
print(np.random.randint(1,10))
print(np.random.randint(1,10,(2,3)))
print(np.random.randint(1,10,(2,3,4)))

# It can also generate negative values
print(np.random.randn(2,2))

a=np.arange(1,11)
print(np.random.choice(a))