a=10
def f1():
  global a
  a=777
  print(a)
def f2():
   print(a)
f1()
f2()
# 777
# 777

# Recursive Functions
# A function that calls itself is known as Recursive Function.

# factorial(3)=3*factorial(2)
# =3*2*factorial(1)
# =3*2*1*factorial(0)
# =3*2*1*1
# =6
# factorial(n)= n*factorial(n-1)

#Anonymous Functions:
#Sometimes we can declare a function without any name,such type of nameless functions
#are called anonymous functions or lambda functions.

#lambda Function :
#We can define by using lambda keyword
#lambda n:n*n

s=lambda n:n*n
print("The Square of 4 is :",s(4))
print("The Square of 5 is :",s(5))
# out-The Square of 4 is : 16
# The Square of 5 is : 25

s=lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:",s(10,20))
print("The Biggest of 100,200 is:",s(100,200))
# out-The Biggest of 10,20 is: 20
# The Biggest of 100,200 is: 200

#filter() function:
#We can use filter() function to filter values from the given sequence based on some
#condition.
#filter(function,sequence)
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1) #[0,10,20,30]
l2=list(filter(lambda x:x%2!=0,l))
print(l2) #[5,15,25]
#map() function:
#For every element present in the given sequence,apply some functionality and generate
#new element with the required modification. For this requirement we should go for
#map() function.

#map(function,sequence)
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1) #[2, 4, 6, 8, 10]

l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1)
#[1, 4, 9, 16, 25]
#We can apply map() function on multiple lists also.But make sure all list should have same
#length.
#Syntax: map(lambda x,y:x*y,l1,l2))
#x is from l1 and y is from l2
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)
#[2, 6, 12, 20]

# reduce() function:
# reduce() function reduces sequence of elements into a single element by applying the
# specified function.
# reduce(function,sequence)

from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result) # 150
#Function Aliasing:
#For the existing function we can give another name, which is nothing but function aliasing.

def wish(name):
   print("Good Morning:",name)
greeting=wish
print(id(wish))
print(id(greeting))
greeting('vishnu')
wish('anushka')
# out-140216763762000
# 140216763762000
# Good Morning: vishnu
# Good Morning: anushka

# Nested Functions:
# We can declare a function inside another function, such type of functions are called Nested
# functions.

def outer():
   print("outer function started")
   def inner():
      print("inner function execution")
   print("outer function calling inner function")
   inner()
outer()
# outer function started
# outer function calling inner function
# inner function execution

# Function Decorators:
# Decorator is a function which can take a function as argument and extend its functionality
# and returns modified function with extended functionality.
def decor(func):
   def inner(name):
      if name=="Sunny":
          print("Hello Sunny Bad Morning")
      else:
        func(name)
   return inner
@decor
def wish(name):
  print("Hello",name,"Good Morning")
wish("vishnu")
wish("anshka")
wish("vishnu")
# out-Hello vishnu Good Morning
# Hello anshka Good Morning
# Hello vishnu Good Morning

# Generators
# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values.
def mygen():
   yield 'A'
   yield 'B'
   yield 'C'
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

# out-<class 'generator'>
# A
# B
# C
