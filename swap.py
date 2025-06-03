'''a=5
b=10
print("before swapping")
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("After swapping")
print("a=",a)
print("b=",b)'''
#factorial of number
'''num=int(input())
factorial=1
if num<0:
    print("no factors")
elif num==0:
    print("0 factor is 1")
else:
    for i in range(1,num+1):
        factorial*=i
print(f"The factorial of {num} if {factorial}")'''
#print First 5 N Natural numbers
'''n=int(input())
if n<=0:
    print("Provide positive numbers")
else:
    for i in range(1,n+1):
        print(i)'''
#sum of first 5 natural numbers
n=int(input())
if n<0:
    print("Provide positive number")
else:
    sum=n*(n+1)//2
    print(sum)
