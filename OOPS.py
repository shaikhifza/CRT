# abstraction:
from abc import ABC,abstractmethod
class four_wheeler(ABC):
    @abstractmethod
    def engine():
        return "hello this is process of making how car engine works"
class swift(four_wheeler):
    def car_start():
        return "Car is moving"
car1=swift
ans=car1.car_start()
print(ans)
#--------
class calculator:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
object=calculator
print(object.add(10,20))
print(object.sub(10,20))
print(object.mul(20,40))
print(object.div(0,9))

ch=int(input("enter your choice"))
if(ch==1):
    print(object.add(13,89))
elif(ch==2):
    print(object.sub(23,22))
elif(ch==3):
    print(object.mul(8,9))
else:
    print(object.div(1,10))
    
# bank application
class Bank_Application:
    def _init_(self,name):
        self.name=name
        self.__balance=0
    def deposit(self):
       amount=int(input("Enter the money"))
       self.balance+=amount
       print(f"{amount} deposited successful. current balance{self.balance}")
    def withdraw(self):
        amount=int(input("Enter the money"))
        if amount>self.balance:
            print(f"{amount} Insufficient Balance")
        else:
            self.balance-=amount
            print(f"{amount} withdraw successfully. Remaining balance is Rs.{self.balance}")        
    def balance(self):
        print(f"Current Balance: {self.balance}")
    def exit(self):
        print("Thanks for using ATM ")  
bank_apply=Bank_Application(initial_balance=35000)
while True:
    print("1.Deposit")
    print("2.withdraw")
    print("3.Current_balance")
    print("4.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        bank_apply.deposit()
    elif choice==2:
        bank_apply.withdraw()
    elif choice==3:
        bank_apply.balance()
    elif choice==4:
        bank_apply.exit()
    else:
        print("Invalid Data")

#--------------
# encapsulation: 

class Student:
    def _init_(self,marks):   #default constructer
        self.marks=marks
        self.__marks=marks  #private 
    def getter(self):
        return self.__marks
    def setter(self,marks):
        self.__marks=marks
obj=Student(0)
obj.setter(99)
ans=obj.getter()
print(ans)
#---------
class father:
    def father_method():
        return "This is father method"
#inheriting father class
class child(father):
    def child_method():
        return "This is child method"
parent_object=father
child_object=child
print(parent_object.father_method())
print(child_object.child_method())
print(child_object.father_method())

# multiple inheritence
class father:
    def father_method():
        return "This is father method"
class mother:
    def mother_method():
        return "This is mother method"
class child(father,mother):
    def child_method():
        return "I have properties of mother and father"
    
father_obj=father
mother_obj=mother
child_obj=child
print(father_obj.father_method())
print(mother_obj.mother_method())
print(child_obj.father_method())
print(child_obj.mother_method())
print(child_obj.child_method())

# multi-level inheritence
class Grand_father:
    def grand_father_method():
        return "This is the Grand Father Method"
class Father(Grand_father):
    def father_method():
        return "This is the Father method"
class child(Grand_father,Father):
    def child_method():
        return "I have properties of both Grand father and father"
grand_father_obj=Grand_father
father_obj=Father
child_obj=child
print(child_obj.grand_father_method())
print(child_obj.father_method())
print(child_obj.child_method())

# hybrid inheritence
class Grand_father:
    def grand_father_method():
        return "This is Grand father method"
class Father(Grand_father):
    def father_method():
        return "This is father method"
class Mother:
    def mother_method():
        return "This is mother method"
class child(Father,Mother,Grand_father):
    def child():
        return "I have properties of all"
grand_father_obj=Grand_father
father_obj=Father
mother_obj=Mother
child_obj=child
print(grand_father_obj.grand_father_method())
print(father_obj.grand_father_method())   
print(father_obj.father_method())
print(child_obj.grand_father_method())
print(child_obj.mother_method())
print(child_obj.father_method())
#---------------
class Animal:
    def speak():
        return "Animal is speaking"
class bird():
    def speak():
        return "bird is speaking"
animal_obj=Animal
bird_obj=bird
print(animal_obj.speak())
print(bird_obj.speak())
