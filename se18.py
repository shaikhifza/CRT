'''def square(x):
    return x*x
res=square(4)
print(res)'''
#lambda function
f=lambda x:x*x
print(f(5))
#normal function to add 2 numbers
def sum(a,b):
    return a+b
c=sum(10,10)
print(c)
#lambda of sum of numbers
c=lambda a,b:a+b
print(c(10,10))
#even or not with normal function
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
f=even(5)
print(f)
#using lambda function
f=lambda num:'even' if num%2==0 else 'odd'
print(f(2))
#create a lambda that returns even numbers
mylst=[1,2,3,4,6,8,9,20,24]
obj=filter(lambda x:x%2==0,mylst)
print(list(obj))
#return squares using lambda
mylst=[1,2,3,4,6,8,9,20,24]
obj=map(lambda x:x*x,mylst)
print(list(obj))
#reduce using lambda funtion for product
lst=[1,2,4,6,-6,7,7.5,8]
from functools import*
result=reduce(lambda x,y:x*y,lst)
print('cumulative product=',result)









