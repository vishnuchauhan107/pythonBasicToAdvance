# How to delete static variables of a class:
# We can delete static variables from anywhere by using the following syntax
# del classname.variablename
# But inside classmethod we can also use cls variable
# del cls.variablename
class Test:
  a=10
  @classmethod
  def m1(cls):
     del cls.a
Test.m1()
print(Test.__dict__)
# out-{'__module__': '__main__', 'm1': <classmethod object at 0x7fe960ad6dc0>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

'''import sys
class Customer:
  bankname='SBI'
  def __init__(self,name,balance=0.0):
    self.name=name
    self.balance=balance
  def deposit(self,amt):
    self.balance=self.balance+amt
    print('Balance after deposit:',self.balance)
  def withdraw(self,amt):
    if amt>self.balance:
       print('Insufficient Funds..cannot perform this operation')
       sys.exit()
    self.balance=self.balance-amt
    print('Balance after withdraw:',self.balance)
print('Welcome to',Customer.bankname)
name=input('Enter Your Name:')
c=Customer(name)
while True:
  print('d-Deposit \nw-Withdraw \ne-exit')
  option=input('Choose your option:')
  if option=='d' or option=='D':
    amt=float(input('Enter amount:'))
    c.deposit(amt)
  elif option=='w' or option=='W':
    amt=float(input('Enter amount:'))
    c.withdraw(amt)
  elif option=='e' or option=='E':
    print('Thanks for Banking')
    sys.exit()
  else:
    print('Invalid option..Plz choose valid option')
    
    # out-Welcome to SBI
    # Enter Your Name:vishnu
    # d-Deposit 
    # w-Withdraw 
    # e-exit
    # Choose your option:d
    # Enter amount:1000
    # Balance after deposit: 1000.0
    # d-Deposit 
    # w-Withdraw 
    # e-exit
    # Choose your option:d
    # Enter amount:288
    # Balance after deposit: 1288.0
    # d-Deposit 
    # w-Withdraw 
    # e-exit
    # Choose your option:'''

#Local variables:
#Sometimes to meet temporary requirements of programmer,we can declare variables inside a
#method directly,such type of variables are called local variable or temporary variables.

class Test:
  def m1(self):
     a=1000
     print(a)
  def m2(self):
     b=2000
     print(b)
t=Test()
t.m1()
t.m2()
# out-1000
# 2000

# Types of Methods:
# Inside Python class 3 types of methods are allowed
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods

# 1. Instance Methods:
# Inside method implementation if we are using instance variables then such type of methods are
# called instance methods.
# Inside instance method declaration,we have to pass self variable.
# def m1(self):


# Setter and Getter Methods:
# We can set and get the values of instance variables by using getter and setter methods.

# Setter Method:
# setter methods can be used to set values to the instance variables. setter methods also known as
# mutator methods.
# syntax:
# def setVariable(self,variable):
#   self.variable=variable
# Getter Method:
# Getter methods can be used to get values of the instance variables. Getter methods also known as
# accessor methods.
# syntax:
# def getVariable(self):
#    return self.variable

'''
class Student:
  def setName(self,name):
     self.name=name
  def getName(self):
     return self.name
  def setMarks(self,marks):
     self.marks=marks
  def getMarks(self):
     return self.marks
n=int(input('Enter number of students:'))
for i in range(n):
  s=Student()
  name=input('Enter Name:')
  s.setName(name)
  marks=int(input('Enter Marks:'))
  s.setMarks(marks)
  print('Hi',s.getName())
  print('Your Marks are:',s.getMarks())
  print()
  
  # out-Enter number of students:2
  # Enter Name:vishnu
  # Enter Marks:90
  # Hi vishnu
  # Your Marks are: 90
  # 
  # Enter Name:anushka
  # Enter Marks:90
  # Hi anushka
  # Your Marks are: 90'''

# 2. Class Methods:
# Inside method implementation if we are using only class variables (static variables), then such type
# of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.

class Animal:
  legs=4
  @classmethod
  def walk(cls,name):
    print('{} walks with {} legs...'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')
#out-Dog walks with 4 legs...
#Cat walks with 4 legs...

# 3. Static Methods:
# In general these methods are general utility methods.
# Inside these methods we won't use any instance or class variables.
# Here we won't provide self or cls arguments at the time of declaration.
# We can declare static method explicitly by using @staticmethod decorator

class vishnuMath:
  @staticmethod
  def add(x,y):
      print('The Sum:', x + y)
      print('The Sum:', x + y)
  @staticmethod
  def product(x, y):
     print('The Product:', x * y)
  @staticmethod
  def average(x, y):
     print('The average:', (x + y) / 2)
vishnuMath.add(10,20)
vishnuMath.product(10,20)
vishnuMath.average(10,20)
# out-The Sum: 30
# The Sum: 30
# The Product: 200
# The average: 15.0


# Inner classes:
# Sometimes we can declare a class inside another class,such type of classes are called inner classes.
# class Car:
# .....
# class Engine:
# ......
class Outer:
  def __init__(self):
     print("outer class object creation")
  class Inner:
     def __init__(self):
        print("inner class object creation")
     def m1(self):
        print("inner class method")
o=Outer()
i=o.Inner()
i.m1()
# out-outer class object creation
# inner class object creation
# inner class method

