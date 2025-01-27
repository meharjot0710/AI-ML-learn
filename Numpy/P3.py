# importing numpy
import numpy as np

# np.arange(start,end,step) works just like the for loop
a=np.arange(1,20)
print(a)
b=np.arange(2,20,2)
print(b)

# b.reshape((rows,columns)) reshapes the array 
b=b.reshape((3,3))
print(b)
a=a.reshape((1,-1))
print(a)
a=a.reshape((-1,1))
print(a)

# b.flatten() makes the array one dimensional with only 1 row but it returns a copy of the original array
b=b.flatten()
print(b)

# b.ravel() does the same work as a.flatten() but it returns only reference of the original array
b=b.ravel()
print(b)





# The basic difference between .flatten() and .ravel() in NumPy is:

# flatten(): Always returns a copy of the array.
# ravel(): Returns a view of the array (if possible). If a view cannot be returned (e.g., for non-contiguous arrays), it returns a copy.
# This means .ravel() is more memory-efficient compared to .flatten() when a view is possible.



# Task

# Task Objective: Indexing and Broadcasting

# Create a 5x5 NumPy array with random integers between 1 and 50.
# Perform the following:
# Extract the second and fourth rows.
# Replace all values greater than 25 with 0 using broadcasting.
# Extract all elements from the third column.

a=np.random.randint(1,51,size=(5,5))
print(a)
row_3_4=a[[1,3], :]
print(row_3_4)
a[a>25]=0
print(a)
b=a[:,2]
print(b)

# Bonus Challenge:
 
# Multiply the extracted third column by 2 and replace the original column in the array.

a[:,2]=b*2
print(a)