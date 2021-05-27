'''
Modules
A group of functions, variables and classes saved to a file, which is nothing but module.
Every Python file (.py) acts as a module.
If we want to use members of module in our program then we should import that module.
import modulename
We can access members by using module name.
modulename.variable
modulename.function()
'''
import vishnumath
print(vishnumath.x)
vishnumath.add(10, 20)
vishnumath.product(10, 20)
# The Sum: 30
# The Product: 200

# Renaming a module at the time of import (module aliasing):
# Eg:
# import durgamath as m

import vishnumath as m
print(m.x)
m.add(10,20)
m.product(10,20)
# out-The Sum: 30
# The Product: 200
# from ... import:
# We can import particular members of module by using from ... import .

from vishnumath import *
print(x)
add(10,20)
product(10,20)
# out-The Sum: 30
# The Product: 200

# Reloading a Module:
# By default module will be loaded only once eventhough we are importing multiple
# multiple times.

print("This is test module")
# out-This is from module1
# This is test module

# Finding members of module by using dir() function:
# Python provides inbuilt function dir() to list out all members of current module or a
# specified module.
# dir() ===>To list out all members of current module
# dir(moduleName)==>To list out all members of specified module

x=10
y=20
def f1():
  print("Hello")
print(dir())
# out-Output
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__nam
# e__', '__package__', '__spec__', 'f1', 'x', 'y']

import vishnumath
print(dir(vishnumath))
# out-['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'product', 'x']

# The Special variable __name__:
import module1
module1.f1()
# out-The code executed as a module from some other program
# Working with math module:
# Python provides inbuilt module math.
# This module defines several functions which can be used for mathematical operations.
# The main important functions are
# 1. sqrt(x)
# 2. ceil(x)
# 3. floor(x)
# 4. fabs(x)
# 5.log(x)
# 6. sin(x)
# 7. tan(x)

from math import *
print(sqrt(4))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))
# out-2.0
# 11
# 10
# 10.6
# 10.6

#We can find help for any module by using help() function
#import math
#help(math)
# Working with random module:
# This module defines several functions to generate random numbers.

# 1. random() function:
# This function always generate some float value between 0 and 1 ( not inclusive)
# 0<x<1

from random import *
for i in range(5):
  print(random())
  # 0.07990074114281398
  # 0.36859019598438514
  # 0.5902214425800926
  # 0.9577999234654806
  # 0.6404993189190803

#2. randint() function:
#To generate random integer beween two given numbers(inclusive)

from random import *
for i in range(5):
   print(randint(1,100))
   # out-100
   # 20
   # 7
   # 70
   # 71

# 3. uniform():
# It returns random float values between 2 given numbers(not inclusive)

from random import *
for i in range(5):
  print(uniform(1,10))

  # out-6.214877805639371
  # 3.669898315818035
  # 2.704137828767613
  # 4.934829371087529
  # 1.1521706622802723


# 5. choice() function:
# It wont return random number.
# It will return a random object from the given list or tuple.
from random import *
list=["Sunny","Bunny","Chinny","Vinny","pinny"]
for i in range(10):
   print(choice(list))
   # outChinny
   # pinny
   # Sunny
   # Vinny
   # Chinny
   # pinny
   # pinny
   # Bunny
   # Sunny
   # Bunny
