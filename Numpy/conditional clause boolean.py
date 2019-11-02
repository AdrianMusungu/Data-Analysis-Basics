import numpy as np

x = np.array([100,400,500,600]) #each member 'a'
y = np.array([10,15,20,25]) #each member 'b'
condition = np.array([True,True,False,False]) #each menber cond

#use loops indirectly to perform this

z = [a if cond else b for a,cond,b in zip(x,condition,y)]
print 'z:'
print z

#np.where(#condition,#value for yes, #value for No)
z2 = np.where(condition,x,y)
print 'z2:'
print z2

z3 = np.where(x>0,0,1)
print 'z3:'
print z3


#Standard functions of numpy

#sum x
print'x.sum:'
print x.sum()

n = np.array([[1,2],[3,4]])

#column sum
print'n.sum:'
print n.sum(0)

print 'x.mean:'
print x.mean()
print'x.std:'
print x.std()
print'x.var:'
print x.var()

#logical operations - and / or operations

condition2 = np.array([False,False])

print 'condition2.any:'
print condition2.any() #or operator
print 'condition2.all:'
print condition2.all() #and operator

#sorting in numpy arrays

unsorted_array = np.array([1,2,8,10,7,3])
unsorted_array.sort()
print 'sorted array:'
print unsorted_array

arr2 = np.array(['solid','solid','solid','liquid','liquid','gas','gas'])
print 'np.unique:'
print np.unique(arr2)
print 'np.in1d:'
print np.in1d(['solid','gas','plasma'],arr2)