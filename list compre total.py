#create a list comprehension to find square of numbers (Normal Method)
lst=[]
for i in range(1,11):
    lst.append(i*i)
print(lst)
#list comprehension method(compact code)
lst=[i*i for i in range(1,11)]
print(lst)
#create a list comprehension to get even nos from 1 to 10
lst=[]
for i in range(2,11,2):
    lst.append(i)
print(lst)
#other way
lst=[]
for i in range(1,11):
    if i%2==0:
        lst.append(i)
print(lst)
#list comprehension method(compact code)
lst=[i for i in range(1,11) if i%2==0]
print(lst)
#list comprehension method(compact code)
lst=[i for i in range(2,11,2)]
print(lst)
#add two list and store them in another list
a=[34,45,6,7,5]
b=[2,4,5,6,7]
c=[]
for i in range(5):
    c.append(a[i]+b[i])
print(c)
#list comprehension method(compact code)
a=[34,45,6,7,5]
b=[2,4,5,6,7]
c=[]
lst=[a[i]+b[i] for i in range(5)]
print(lst)
#retrive common elements
a=[34,45,6,7,5]
b=[2,4,5,6,7]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)
#list comprehension method(compact code)
a=[34,45,6,7,5]
b=[2,4,5,6,7]
c=[i for i in a if i in b]
print(c)
#retrive only first letter of each word
a=['hifza','nafeessa','umar','haseena','munavar']
b=[]
for i in a:
    b.append(i[0])
print(b)
#list comprehension method(compact code)
a=['hifza','nafeessa','umar','haseena','munavar']
b=[i[0] for i in a]
print(b)




