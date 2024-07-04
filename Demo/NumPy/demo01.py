import numpy as np
#
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(type(a))

a=np.array([2,3,4])
print(a)
print(a.dtype)
b=np.array([1,2,3,5,5,1])
print(b.dtype)

array1=np.array(((1,2,3),(2,3,4)))
print(array1)
c=np.array([[1,2,3],[1.2,3.5,6]],dtype=np.float64)
print(c)
array_zeros = np.zeros((3, 4))
print(array_zeros)
array_ones=np.ones((2,3,4),dtype=np.int16)
print(array_ones)

array_empty=np.empty((2,3))
print(array_empty)
array_arange=np.arange(10,30,5)
print(array_arange)
array_linspace=np.linspace(0,2,9)
print(array_linspace)
x=[1,2,3]
a=np.asarray(x,dtype=np.float64)
print(a)

array_identity=np.identity(3)
print(array_identity)

array_diag=np.diag([1,2,3])
print(array_diag)


