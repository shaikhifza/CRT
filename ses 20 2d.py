from numpy import *
arr=array([[3,4,5],[7,6,2],[1,7,2]])
print(arr)
#using ones and zeros
arr=ones((3,4),int)
print(arr)
arr=zeros((3,4))
print(arr)
x=eye(5,dtype=int)
print(x)
#indexing and slicing
from numpy import *
a=array([[5,4,3],[6,8,7],[3,1,2]])
print(a[0])
print(a[1])
print(a[0:2,0:2])
#matrices
str='1 2 3 4 5 6'
m1=matrix(str)
print(m1)
arr=array([[3,4,5],[7,6,2],[1,7,2]])
m=matrix(arr)
print(m)
arr=diagonal(m)
print(arr)
#multiply 2 matrix
m=array([[5,4,3],
    [6,8,7],
    [3,1,2]])
m1=m.T
print(m1)
print(m*m1)
#by taking input to find transpose
from numpy import*
r,c=[int(i)for i in input('how many elements').split()]
arr=zeros((r,c),int)
print('enter elements:')
for i in range(r):
                          arr[i]=[int(i)for i in input().split()]
                          m=matrix(arr)
                          print('Transpose matrix:')
                          m1=m.transpose()
                          print(m1)
                
                          
