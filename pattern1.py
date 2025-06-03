#pattern 1
'''for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()'''
#pattern 2
'''for i in range(4):
    for j in range(4):
        if i==j:
            print('$',end=" ")
        else:
            print("*",end=" ")
    print()'''
#pattern 3
'''for i in range(1,5):
    for j in range(1,5):
        print(j+(i-1)*4,end="\t")
    print()'''
#pattern 4
'''for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#pattern 5
'''for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print(j+(i-1)*4,end="\t")
        else:
            print(" ",end="\t")
    print()
    print()'''
#pattern 6
'''for i in range(1,5):
    for j in range(1,5):
        if i<j:
            print(" ",end=" ")
        else:
            print("x",end=" ")
    print()'''
#pattern 7
'''for i in range(1,5):
    for j in range(1,5):
        if j>i:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#pattern 8
'''for i in range(1,5):
    for j in range(1,5):
        if i+j>=5:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#pattern 9
'''for i in range(1,5):
    for j in range(1,5):
        if i+j<5:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#with one for loop
'''for i in range(4,0,-1):
    print(" x "*i)'''
#pattern 10
'''for i in range(1,5):
    for j in range(1,5):
        if i<j:
            print(" ",end=" ")
        else:
            print(j,end=" ")
    print()'''
#pattern 11
'''for i in range(4,0,-1):#rows
    for j in range(0,4-i):#columns
        print(end=" ")#space printing
    for j in range(0,i):#for x printing
        print("x",end=" ")
    print()'''
#pattern 12
'''for i in range(0,5):#rows
    for j in range(0,4-i):#columns
        print(end=" ")#space printing
    for j in range(0,i):#for x printing
        print("x",end=" ")
    print()'''
#pattern 13
'''for i in range(4,0,-1):
    for j in range(0,4-i):
        print(end=" ")
    for j in range(0,i):
        print("x",end=" ")
    print()
for i in range(0,5):
    for j in range(0,4-i):
        print(end=" ")
    for j in range(0,i):
        print("x",end=" ")
    print()'''
#pattern 14
'''for i in range(1,6):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()'''
#pattern 15
'''string="ABCD"
for i in range(5):
    for j in range(i):
            print(string[j],end=" ")
    print()'''
#pattern 15(Not Done YET)
'''string="ABCD"
for i in range(5,0,-1):
    for j in range(i-4):
            print(string[j],end=" ")
    print()'''
#Diamond pattern





