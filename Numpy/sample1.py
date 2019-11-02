import numpy as np

my_list1 = [1,2,3,4]
my_list2 = [5,6,7,8]
a = [10,20,20,40]
b = [30,40,50,60]
c = ['a','b','c','d']
#print a
a2 = np.array([a])
#print a2.shape

#my_array = np.array(my_list1)

#my_array = np.array([my_list1,my_list2])
#print my_array

#usage of shape function
#print my_array.shape

#finding out the datatype of the members of the array
#print a2.dtype

#zeros, ones, empty, eye, arange

#new_array1 = np.zeros([5,2]) #creates a new numpy array with (1*5). All elements are zero
#new_array1 = np.ones([5,5]) #all elements as 1
#new_array1 = np.empty(4) #creates an empty array of 10^-315, which tends to zero
#new_array1 = np.eye(5)
new_array1 = np.arange(2,20,5)
#print (new_array1)

#slices of 2d array
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
#slice1 = x[1:2,1:3]
#print slice1

#x[1:2,:2] = 10
#print x
#print x[[0,2],[0,2]]

arr_len = x.shape[0]

for i in range(arr_len):
    x[i] = i
#print x
c = [1,21,3]
d = [10,20,30]
e = [100,-2,5]

#print np.maximum(c, d)

#print np.maximum.reduce([c,d,e])

#save one array to *.npy file
arr = np.array([3,6,9])
np.save('arrayof3', arr)
loader1 = np.load('arrayof3.npy')
print loader1

#save 2 arrays to *.npz file
arr2 = np.array([4,8,12])
np.savez('arrayof3&4', x= arr, y= arr2)
loader2 = np.load('arrayof3&4.npz')
print loader2['y']

#save arrays to text file
np.savetxt('arrayof3.txt',arr, delimiter=',')
loader3 = np.loadtxt('arrayof3.txt', delimiter=',')
print loader3

