'''
If a group of statements is repeatedly required then it is not recommended to write these
statements everytime seperately.
Python supports 2 types of functions
1. Built in Functions
2. User Defined Functions
1. Built in Functions:
The functions which are coming along with Python software automatically,are called built
in functions or pre defined functions
Eg:
id()
type()
input()
eval()

2. User Defined Functions:
The functions which are developed by programmer explicitly according to business
requirements ,are called user defined functions.
Syntax to create user defined functions:
def function_name(parameters) :
""" doc string"""
----
-----
return value
'''
def wish():
 print("Hello Good Morning")
wish()
wish()
wish()
# out-Hello Good Morning
# Hello Good Morning
# Hello Good Morning


def wish(name):
  print("Hello",name," Good Morning")
wish("vishnu")
wish("anushka")
# Hello vishnu  Good Morning
# Hello anushka  Good Morning

# Return Statement:
# Function can take input values as parameters and executes business logic, and returns
# output to the caller with return statement.

def add(x,y):
  return x+y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))

# out-The sum is 30
# The sum is 300

#Returning multiple values from a function:
def calc(a,b):
  sum=a+b
  sub=a-b
  mul=a*b
  div=a/b
  return sum,sub,mul,div
t=calc(100,50)
print("The Results are")
for i in t:
  print(i)
  # out-The Results are
  # 150
  # 50
  # 5000
  # 2.0

# Types of arguments
# def f1(a,b):
# ------
# ------
# ------
# f1(10,20)
# a,b are formal arguments where as 10,20 are actual arguments

# There are 4 types are actual arguments are allowed in Python.
# 1. positional arguments
# 2. keyword arguments
# 3. default arguments
# 4. Variable length arguments


# 1. positional arguments:
# These are the arguments passed to function in correct positional order.

def sub(a,b):
  print(a-b)
sub(100,200)
sub(200,100)
# out--100
# 100

# 2. keyword arguments:
# We can pass argument values by keyword i.e by parameter name.

def wish(name, msg):
  print("Hello", name, msg)
wish(name="vishnu", msg="Good Morning")
wish(msg="Good Morning", name="anushka")
# out-Hello vishnu Good Morning
# Hello anushka Good Morning

#3. Default Arguments:
#Sometimes we can provide default values for our positional arguments.

def wish(name="Guest"):
  print("Hello", name, "Good Morning")
wish("vishnu")
wish()
# out-Hello vishnu Good Morning
# Hello Guest Good Morning

# 4. Variable length arguments:
# Sometimes we can pass variable number of arguments to our function,such type of
# arguments are called variable length arguments.
# We can declare a variable length argument with * symbol as follows
# def f1(*n):

def sum(*n):
  total = 0
  for n1 in n:
    total = total + n1
  print("The Sum=", total)
sum()
sum(10)
sum(10, 20)
sum(10, 20, 30, 40)

# out-The Sum= 0
# The Sum= 10
# The Sum= 30
# The Sum= 100

def f1(*s, n1):
  for s1 in s:
    print(s1)
  print(n1)
f1("A", "B", n1=10)
# A
# B
# 10

# Note: Function vs Module vs Library:
# 1. A group of lines with some name is called a function
# 2. A group of functions saved to a file , is called Module
# 3. A group of Modules is nothing but Library

# Types of Variables
# Python supports 2 types of variables.
# 1. Global Variables
# 2. Local Variables

# 1. Global Variables
# The variables which are declared outside of function are called global variables.
# These variables can be accessed in all functions of that module.

a=10 # global variable
def f1():
  print(a)
def f2():
  print(a)
f1()
f2()
# out-10
# 10
# 10

# 2. Local Variables:
# The variables which are declared inside a function are called local variables.
# Local variables are available only for the function in which we declared it.i.e from outside
# of function we cannot access.

def f1():
  a = 10
print(a)# 10
