#Poly means many. Morphs means forms.
#Polymorphism means 'Many Forms'.


# 1. Duck Typing Philosophy of Python:
# def f1(obj):
# obj.talk()
class Duck:
  def talk(self):
     print('Quack.. Quack..')
class Dog:
  def talk(self):
    print('Bow Bow..')
class Cat:
   def talk(self):
      print('Moew Moew ..')
class Goat:
    def talk(self):
       print('Myaah Myaah ..')
def f1(obj):
  obj.talk()
l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
  f1(obj)
  # out-Quack.. Quack..
  # Moew Moew ..
  # Bow Bow..
  # Myaah Myaah .

# Demo Program with hasattr() function:
class Duck:
  def talk(self):
    print('Quack.. Quack..')
class Human:
  def talk(self):
     print('Hello Hi...')
class Dog:
   def bark(self):
      print('Bow Bow..')
def f1(obj):
  if hasattr(obj,'talk'):
    obj.talk()
  elif hasattr(obj,'bark'):
     obj.bark()
d=Duck()
f1(d)
h=Human()
f1(h)
d=Dog()
f1(d)
# out-Quack.. Quack..
# Hello Hi...
# Bow Bow..

# Overloading:
# We can use same operator or methods for different purposes.
# There are 3 types of overloading
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading

# 1. Operator Overloading:
# We can use the same operator for multiple purposes, which is nothing but operator overloading.
# Python supports operator overloading.

'''class Book:
  def __init__(self,pages):
    self.pages=pages
b1=Book(100)
b2=Book(200)
print(b1+b2)'''

class Book:
  def __init__(self,pages):
    self.pages=pages
  def __add__(self,other):
    return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print('The Total Number of Pages:',b1+b2)
# out-The Total Number of Pages: 300

# The following is the list of operators and corresponding magic methods.
# + ---> object.__add__(self,other)
# - ---> object.__sub__(self,other)
# * ---> object.__mul__(self,other)
# / ---> object.__div__(self,other)
# // ---> object.__floordiv__(self,other)
# % ---> object.__mod__(self,other)
# ** ---> object.__pow__(self,other)
# += ---> object.__iadd__(self,other)
# -= ---> object.__isub__(self,other)
# *= ---> object.__imul__(self,other)
# /= ---> object.__idiv__(self,other)
# //= ---> object.__ifloordiv__(self,other)
# %= ---> object.__imod__(self,other)
# **= ---> object.__ipow__(self,other)
# < ---> object.__lt__(self,other)
# <= ---> object.__le__(self,other)
# > ---> object.__gt__(self,other)
# >= ---> object.__ge__(self,other)


# Overloading > and <= operators for Student class objects:
class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def __gt__(self,other):
    return self.marks>other.marks
  def __le__(self,other):
    return self.marks<=other.marks
print("10>20 =",10>20)
s1=Student("Durga",100)
s2=Student("Ravi",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1<=s2=",s1<=s2)
print("s1>=s2=",s1>=s2)
# out-10>20 = False
# s1>s2= False
# s1<s2= True
# s1<=s2= True
# s1>=s2= False

class Employee:
  def __init__(self,name,salary):
     self.name=name
     self.salary=salary
  def __mul__(self,other):
     return self.salary*other.days
class TimeSheet:
    def __init__(self,name,days):
       self.name=name
       self.days=days
e=Employee('vishnu',500)
t=TimeSheet('vishnu',25)
print('This Month Salary:',e*t)
# out-This Month Salary: 12500


# 2. Method Overloading:
# If 2 methods having same name but different type of arguments then those methods are said to
# be overloaded methods.
class Test:
  def m1(self):
     print('no-arg method')
  def m1(self,a):
     print('one-arg method')
  def m1(self,a,b):
     print('two-arg method')
t=Test()
#t.m1()
#t.m1(10)
t.m1(10,20)
# out-two-arg method

# How we can handle overloaded method requirements in Python:
class Test:
  def sum(self,*a):
    total=0
    for x in a:
      total=total+x
      print('The Sum:',total)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()
# out0The Sum: 10
# The Sum: 30
# The Sum: 10
# The Sum: 30
# The Sum: 60
# The Sum: 10

# 3. Constructor Overloading:
# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.

class Test:
  def __init__(self):
     print('No-Arg Constructor')
  def __init__(self,a):
     print('One-Arg constructor')
  def __init__(self,a,b):
     print('Two-Arg constructor')
#t1=Test()
#t1=Test(10)
t1=Test(10,20)
# out-Two-Arg constructor

# Method overriding:
class P:
  def property(self):
    print('Gold+Land+Cash+Power')
  def marry(self):
    print('Appalamma')
class C(P):
   def marry(self):
      print('Katrina Kaif')
c=C()
c.property()
c.marry()
# out-Gold+Land+Cash+Power
# Katrina Kaif

