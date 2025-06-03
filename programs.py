'''#1. Enter id number, name and salary one by one and display them.
id_num=int(input())
salary=float(input())
print("id number= %i" %(id_num))
print("salary= %.2f"%(salary))
#2. Enter 3 numbers and find their sum and average.
a,b,c=[int(i)for i in input().split(",")]
sum=a+b+c
avg=sum/3
print("sum=",sum)
print("avg=",avg)
#3. Enter the radius of a circle and find the area.
rad=int(input())
area=3.14*rad*rad
print("area of a circle=",area)
#4. Enter  a character and display it.
char=input()
print(char)
#5. Enter two strings and display the total string.
s=input()
t=input()
print(s+ t)
#6. Enter a number and display its cube value.
n=int(input())
s=n**3
print(s)
#7.Sort a group of strings into ascending order.  
lst=[i for i in input().split(",")]
lst.sort()
print(lst)'''
#8. Enter a list of different elements and display them.  
lst=[i for i in input().split(",")]
print(lst)
