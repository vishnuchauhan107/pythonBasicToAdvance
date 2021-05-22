# In any programming language there are 2 types of errors are possible.
# 1. Syntax Errors
# 2. Runtime Errors
# 1. Syntax Errors:
# The errors which occurs because of invalid syntax are called syntax errors.

'''
x=10
if x==10
print("Hello")
SyntaxError: invalid syntax
'''

# 2. Runtime Errors:
# Also known as exceptions.
# While executing the program if something goes wrong because of end user input or
# programming logic or memory problems etc then we will get Runtime Errors.

# print(10/0) ==>ZeroDivisionError: division by zero
# print(10/"ten") ==>TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Exception Handling concept applicable for Runtime Errors but not for syntax errors


# What is Exception:
# An unwanted and unexpected event that disturbs normal flow of program is called
# exception.

# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError
# EOFError
# SleepingError
# TyrePuncturedError

print("Hello")
#print(10/0) out-ZeroDivisionError: division by zero
print("Hi")

'''Customized Exception Handling by using try-except:
It is highly recommended to handle exceptions.
The code which may raise exception is called risky code and we have to take risky code
inside try block. The corresponding handling code we have to take inside except block.

try:
Risky Code
except XXX:
Handling code/Alternative Code
'''
print("stmt-1")
try:
  print(10/0)
except ZeroDivisionError:
  print(10/2)
print("stmt-3")
# stmt-1
# 5.0
# stmt-3

# Control Flow in try-except:
# try:
# stmt-1
# stmt-2
# stmt-3
# except XXX:
# stmt-4
# stmt-5

# How to print exception information:
'''print(10/0)
except ZeroDivisionError as msg:\
    print("exception raised and its description is:",msg)'''
#try with multiple except blocks:
try:
  x=10
  y=0
  print(x/y)
except ZeroDivisionError :
  print("Can't Divide with Zero")
except ValueError:
  print("please provide int value only")
  #Can't Divide with Zero

'''try:
  x=10
  y='ten'
  print(x/y)
except ZeroDivisionError :
  print("Can't Divide with Zero")
except ValueError:
  print("please provide int value only")'''


'''try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except ArithmeticError :
   print("ArithmeticError")
except ZeroDivisionError:
   print("ZeroDivisionError")
   out-Enter First Number: 10
Enter Second Number: 0
ArithmeticError'''

# Single except block that can handle multiple exceptions:
# We can write a single except block that can handle multiple different types of exceptions.
# except (Exception1,Exception2,exception3,..): or
# except (Exception1,Exception2,exception3,..) as msg

'''try:
  x=int(input("Enter First Number: "))
  y=int(input("Enter Second Number: "))
  print(x/y)
except (ZeroDivisionError,ValueError) as msg:
  print("Plz Provide valid numbers only and problem is: ",msg)
  # out-Enter First Number: 10
  # Enter Second Number: 0
  # Plz Provide valid numbers only and problem is:  division by zero'''

# Default except block:
# We can use default except block to handle any type of exceptions.
# In default except block generally we can print normal error messages.

try:
   x=10
   y=0
   print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError:Can't divide with zero")
except:
     print("Default Except:Plz provide valid input only")

     # out-ZeroDivisionError:Can't divide with zero

# finally block:
# 1. It is not recommended to maintain clean up code(Resource Deallocating Code or
# Resource Releasing code) inside try block because there is no guarentee for the execution
# of every statement inside try block always.

# Hence the main purpose of finally block is to maintain clean up code.
# try:
# Risky Code
# except:
# Handling Code
# finally:
# Cleanup code
try:
  print("try")
except:
  print("except")
finally:
  print("finally")
  # try
  # finally
try:
  print("try")
  print(10/0)
except ZeroDivisionError:
  print("except")
finally:
  print("finally")
  # out-try
  # except
  # finally

  # If there is an exception raised but not handled:
try:
  print("try")
  print(10/ten)
except NameError:
  print("except")
finally:
  print("finally")
# try
# except
# finally

# Note: There is only one situation where finally block won't be executed ie whenever
# we are using os._exit(0) function.
'''imports
try:
  print("try")
os._exit(0)
  except NameError:
print("except")
  finally:
print("finally")'''

# Control flow in try-except-finally:
# try:
#  stmt-1
#  stmt-2
#  stmt-3
# except:
#  stmt-4
# finally:
#  stmt-5
# stmt6
# Nested try-except-finally blocks:
# We can take try-except-finally blocks inside try or except or finally blocks.i.e nesting of try-
# except-finally is possible.

try:
  print("outer try block")
  try:
    print("Inner try block")
    print(10/0)
  except ZeroDivisionError:
     print("Inner except block")
  finally:
     print("Inner finally block")
except:
  print("outer except block")
finally:
  print("outer finally block")

  # out-outer try block
  # Inner try block
  # Inner except block
  # Inner finally block
  # outer finally block

  # Types of Exceptions:
  # In Python there are 2 types of exceptions are possible.
  # 1. Predefined Exceptions
  # 2. User Definded Exceptions

 # . Predefined Exceptions:
# Also known as in-built exceptions
# The exceptions which are raised automatically by Python virtual machine whenver a
# particular event occurs, are called pre defined exceptions.
# like - zero devision error

# 2. User Defined Exceptions:
# Also known as Customized Exceptions or Programatic Exceptions

# How to Define and Raise Customized Exceptions:
# Every exception in Python is a class that extends Exception class either directly or
# indirectly.
# Syntax:
# class classname(predefined exception class name):
#   def __init__(self,arg):
#       self.msg=arg



