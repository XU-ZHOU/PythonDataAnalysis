import numpy as np
data = np.random.randn(2,3)
print(data)

print(data*10)
print(data+data)

print(data.shape)
print(data.dtype)

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.dtype)

print(np.zeros(10))
print(np.zeros((3,6)))

print(np.empty((2,3,2)))

print(np.arange(15))

arr1 = np.array([1,2,3],dtype=np.float64)
arr2 = np.array([1,2,3],dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)

arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
print(arr)
print(arr.astype(np.int32))

numeric_strings = np.array(['1.25','-9.6','42'],dtype=np.string_)
print(numeric_strings.astype(float))

arr = np.array([[1.,2.,3.],[4.,5.,6.]])
print(arr)

print(arr*arr)

print(arr-arr)

print(1/arr)
arr = np.arange(10)
print(arr)
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)

arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr3d)

print(arr3d[0])

print(arr)

print(arr[1:6])

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

print(arr2d[:2,1:])
print(arr2d[1,:2])
print(arr2d[:2,-1])
print(arr2d[:,:1])

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)
print(names)
print(data)
print(names=='Bob')
print(data[names == 'Bob'])

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)

arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)

arr = np.random.randn(6,3)
print(arr)
np.dot(arr.T,arr)

