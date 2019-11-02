import numpy as np
arr = np.arange(0,12)
print arr

print arr[0:5]
print arr[2:6]

arr[0:5] = 20
print arr

# Interesting thing & Important

arr2 = arr[0:6]

arr2[:] = 29 #all elements are modified

print arr2
print arr

# creating new array copy

arrcopy = arr.copy()
print arrcopy

x = np.array([[10,20,30],[40,60],[70,80,90]])
print x[1][0]