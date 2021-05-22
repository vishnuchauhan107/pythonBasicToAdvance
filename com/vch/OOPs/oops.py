'''
Python's Object Oriented Programming (OOPs)
What is Class:
In Python every thing is an object. To create objects we required some Model or Plan or Blue
print, which is nothing but class.


How to Define a class?
We can define a class by using class keyword.
Syntax:
class className:
    documenttation string '''


class Student:
  def __init__(self):
     self.name='vishnu'
     self.age=19
     self.marks=90
  def talk(self):
      print("Hello I am :",self.name)
      print("My Age is:",self.age)
      print("My Marks are:",self.marks)
# What is Object:
# Pysical existence of a class is nothing but object. We can create any number of objects for a class.
# Syntax to create object: referencevariable = classname()
# Example: s = Student()

# What is Reference Variable:
# The variable which can be used to refer object is called reference variable.
# By using reference variable, we can access properties and methods of object.
class Student:
  def __init__(self, name, rollno, marks):
    self.name = name
    self.rollno = rollno
    self.marks = marks

  def talk(self):
     print("Hello My Name is:", self.name)
     print("My Rollno is:", self.rollno)
     print("My Marks are:", self.marks)

s1=Student("vishnu",68,19)
s1.talk()
# out-Hello My Name is: vishnu
# My Rollno is: 68
# My Marks are: 19
# Constructor Concept:
class Test:
  def __init__(self):
     print("Constructor exeuction...")
  def m1(self):
    print("Method execution...")
t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()
# out-Constructor exeuction...
# Constructor exeuction...
# Constructor exeuction...
# Method execution..

class Student:
  def __init__(self, x, y, z):
    self.name = x
    self.rollno = y
    self.marks = z
  def display(self):
     print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name, self.rollno, self.marks))
s1=Student("vishnu",101,19)
s1.display()
s2=Student("anushka",102,18)
s2.display()

# out-Student Name:vishnu
# Rollno:101
# Marks:19
# Student Name:anushka
# Rollno:102
# Marks:18

# Types of Variables:
# Inside Python class 3 types of variables are allowed.
# 1. Instance Variables:
# If the value of a variable is varied from object to object, then such type of variables are called
# instance variables.
# 1. Inside Constructor by using self variable:

class Employee:
   def __init__(self):
     self.eno = 100
     self.ename = 'vishnu'
     self.esal = 1000
e = Employee()
print(e.__dict__)
# out-{'eno': 100, 'ename': 'vishnu', 'esal': 1000}
# 2. Inside Instance Method by using self variable:

class Test:
  def __init__(self):
    self.a = 10
    self.b = 20
  def m1(self):
    self.c = 30
t = Test()
t.m1()
print(t.__dict__)
# out-{'a': 10, 'b': 20, 'c': 30}

# 3. Outside of the class by using object reference variable:
# We can also add instance variables outside of a class to a particular object.

class Test:
  def __init__(self):
    self.a = 10
    self.b = 20
  def m1(self):
    self.c = 30
t = Test()
t.m1()
t.d = 40
print(t.__dict__)
# out-{'a': 10, 'b': 20, 'c': 30, 'd': 40}


# How to access Instance variables:
class Test:
  def __init__(self):
    self.a = 10
    self.b = 20
  def display(self):
    print(self.a)
    print(self.b)
t = Test()
t.display()
print(t.a, t.b)
# out-10
# 20
# 10 20

# How to delete instance variable from the object:
# 1. Within a class we can delete instance variable as follows
# del self.variableName
# 2. From outside of class we can delete instance variables as follows
# del objectreference.variableName
class Test:
  def __init__(self):
    self.a = 10
    self.b = 20
    self.c = 30
  def m1(self):
     del self.c
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.a
print(t.__dict__)
# out-{'a': 10, 'b': 20, 'c': 30}
# {'a': 10, 'b': 20}
# {'b': 20}


# The instance variables which are deleted from one object,will not be deleted from other
# objects.

class Test:
  def __init__(self):
   self.a=10
   self.b=20
   self.c=30
   self.d=40
t1=Test()
t2=Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)
# out-{'b': 20, 'c': 30, 'd': 40}
# {'a': 10, 'b': 20, 'c': 30, 'd': 40}

class Test:
  def __init__(self):
    self.a=10
    self.b=20
t1=Test()
t1.a=888
t1.b=999
t2=Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
# out-t1: 888 999
# t2: 10 20


# 1. Static variables:
# If the value of a variable is not varied from object to object, such type of variables we have to
# declare with in the class directly but outside of methods. Such type of variables are called Static
# variables.

class Test:
   x=10
   def __init__(self):
     self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
# out-t1: 10 20
# t2: 10 20
# t1: 888 999
# t2: 888 20

'''Various places to declare static variables:
1. In general we can declare within the class directly but from out side of any method
2. Inside constructor by using class name
3. Inside instance method by using class name
4. Inside classmethod by using either class name or cls variable
5. Inside static method by using class name'''

class Test:
  a=10
  def __init__(self):
     Test.b=20
  def m1(self):
     Test.c=30
  @classmethod
  def m2(cls):
    cls.d1=40
    Test.d2=400
  @staticmethod
  def m3():
    Test.e=50
    print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)

# out- '__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7fd0a6789040>, 'm1': <function Test.m1 at 0x7fd0a67890d0>, 'm2': <classmethod object at 0x7fd0a677f1c0>, 'm3': <staticmethod object at 0x7fd0a677f220>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 400, 'e': 50}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7fd0a6789040>, 'm1': <function Test.m1 at 0x7fd0a67890d0>, 'm2': <classmethod object at 0x7fd0a677f1c0>, 'm3': <staticmethod object at 0x7fd0a677f220>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 400, 'e': 50}
# {'__module__': '__main__','a': 10, '__init__': <function Test.__init__ at 0x7fd0a6789040>, 'm1': <function Test.m1 at 0x7fd0a67890d0>, 'm2': <classmethod object at 0x7fd0a677f1c0>, 'm3': <staticmethod object at 0x7fd0a677f220>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 400, 'e': 50, 'f': 60}

# Where we can modify the value of static variable:
class Test:
   a=777
   @classmethod
   def m1(cls):
     cls.a=888
   @staticmethod
   def m2():
     Test.a=999
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
# 777
# 888
# 999
class Test:
  a=10
  def m1(self):
    self.a=888
t1=Test()
t1.m1()
print(Test.a)
print(t1.a)
# 10
# 888

