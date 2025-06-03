#1st way
import numpy as np
arr=np.array([20,30,40,50])
print(arr)
#--------
print(type(arr))
#--------
names=np.array(['hifza',3.444,'1010'])
print(names)
#--------
x=np.array([1.2,3.4,5.5,44])
print(x)
#2nd way
x=np.linspace(0,20,7)
print(x)
#----------
x=np.logspace(1,4,5)
print(x)
#3rd way
a=np.arange(10)
print(a)
#4th way
a1=np.zeros(5,int)
print(a1)
a2=np.zeros(5,float)
print(a2)
a3=np.ones(5)
print(a3)
#operations on array
array=np.array([2,3,4,5])
print(array+5)
print(array-5)
array=np.sqrt([2,3,4,5])
print(array)
array=np.array([2,3,4,5])
print(pow(array,3))
#some more operations
arr=np.array([45,-1,34,3,2])
print(np.sort(arr))
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.sort(arr)[::-1])
#Replace values
arr=np.array([10,20,30,40,55])
print(arr)
b=arr
print(b)
b[0]=99
print(b)
#shallow copying
x=b.view()
print(b)
b[0]=98
print(b)
print(arr)
#deep copying
x=arr.copy()
print(x)
x[0]=222
print(x)
print(arr)
#indexing and slicing
w=np.array([12,34,56,78,90])
print(w[0])
print(w[0:3])
print(w[4:1:-1])
#properties of array
arr=np.array([[12,3,4],
              [3,4,5]])
print(arr.shape)
print(arr.size)
print(arr.nbytes)
print(arr.itemsize)
print(arr.reshape(2,3))
print(arr.reshape(3,2))
print(arr.flatten())
