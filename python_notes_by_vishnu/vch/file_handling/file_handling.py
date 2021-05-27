'''
File Handling
As the part of programming requirement, we have to store our data permanently for
future purpose. For this requirement we should go for files.
Types of Files:
There are 2 types of files
1. Text Files:
Usually we can use text files to store character data
eg: abc.txt
2. Binary Files:
Usually we can use binary files to store binary data like images,video files, audio files etc...
'''

# Opening a File:
# Before performing any operation (like read or write) on the file,first we have to open that
# file.For this we should use Python's inbuilt function open()
# f = open(filename, mode)
'''The allowed modes in Python are
1. r  open an existing file for read operation. The file pointer is positioned at the
beginning of the file.If the specified file does not exist then we will get
FileNotFoundError.This is default mode.
2. w  open an existing file for write operation. If the file already contains some data
then it will be overridden. If the specified file is not already avaialble then this mode will
create that file.
3. a  open an existing file for append operation. It won't override existing data.If the
specified file is not already avaialble then this mode will create a new file.
4. r+  To read and write data into the file. The previous data in the file will not be
deleted.The file pointer is placed at the beginning of the file.
5. w+  To write and read data. It will override existing data.
6. a+  To append and read data from the file.It wont override existing data.
7. x  To open a file in exclusive creation mode for write operation. If the file already
exists then we will get FileExistsError
'''


# Closing a File:
# After completing our operations on the file,it is highly recommended to close the file.
# For this we have to use close() function.
# f.close()

# Various properties of File Object:
# name  Name of opened file
# mode  Mode in which the file is opened
# closed  Returns boolean value indicates that file is closed or not
# readable() Retruns boolean value indicates that whether file is readable or not
# writable() Returns boolean value indicates that whether file is writable or not.

f=open("abc.txt", 'w')
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is File Readable: ",f.readable())
print("Is File Writable: ",f.writable())
print("Is File Closed : ",f.closed)
f.close()
print("Is File Closed : ",f.closed)

# out-File Name:  abc.txt
# File Mode:  w
# Is File Readable:  False
# Is File Writable:  True
# Is File Closed :  False
# Is File Closed :  True

# Writing data to text files:
# We can write character data to the text files by using the following 2 methods.
# write(str)
# writelines(list of lines)

f=open("abcd.txt", 'w')
f.write("vishnu\n")
f.write("Software\n")
f.write("Solutions\n")
print("Data written to the file successfully")
f.close()
# in abcd.txt:
# Durga
# Software
# Solutions
#Data written to the file successfully
f=open("abcd.txt", 'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

# in  abcd.txt:
# sunny
# bunny
# vinny
# chinny

# Note: while writing data by using write() methods, compulsory we have to provide line
# seperator(\n),otherwise total data should be written to a single line.

# Reading Character Data from text files:
# We can read character data from text file by using the following read methods.
# read() To read total data from the file
# read(n)  To read 'n' characters from the file
# readline() To read only one line
# readlines() To read all lines into a list


f=open("abcd.txt", 'r')
data=f.read()
print(data)
f.close()

# out sunny
# bunny
# vinny
# chinny

f=open("abcd.txt", 'r')
data=f.read(10)
print(data)
f.close()
# out-sunny
# bunn

f=open("abcd.txt", 'r')
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close()
# out-sunny
# bunny
# vinny


f=open("abcd.txt", 'r')
lines=f.readlines()
for line in lines:
  print(line,end='')
f.close()
# out-bunny
# vinny
# chinny

f=open("abcd.txt", "r")
print(f.read(3))
print(f.readline())
print(f.read(4))
print("Remaining data")
print(f.read())
# out-sun
# ny
#
# bunn
# Remaining data
# y
# vinny
# chinny

# The with statement:
# The with statement can be used while opening a file.We can use this to group file
# operation statements within a block.

with open("abc.txt", "w") as f:
  f.write("vishnu\n")
  f.write("Software\n")
  f.write("Solutions\n")
print("Is File Closed: ", f.closed)
print("Is File Closed: ", f.closed)
# out-Is File Closed:  True
# Is File Closed:  True

'''The seek() and tell() methods:
tell():
==>We can use tell() method to return current position of the cursor(file pointer) from
beginning of the file. [ can you plese telll current cursor position]
The position(index) of first character in files is zero just like string index.
'''
f=open("abc.txt", "r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())

# out-0
# vi
# 2
# shn
# 5
# seek():
# We can use seek() method to move cursor(file pointer) to specified location.
# [Can you please seek the cursor to a particular location]
# f.seek(offset, fromwhere)

# The allowed values for second attribute(from where) are
# 0---->From beginning of file(default value)
# 1---->From current position
# 2--->From end of the file
data="All Students are STUPIDS"
f=open("abc.txt", "w")
f.write(data)
with open("abc.txt", "r+") as f:
  text = f.read()
  print(text)
  print("The Current Cursor Position: ", f.tell())
  f.seek(17)
  print("The Current Cursor Position: ", f.tell())
  f.write("GEMS!!!")
  f.seek(0)
  text = f.read()
  print("Data After Modification:")
  print(text)

  # out- All Students are STUPIDS
  # The Current Cursor Position:  24
  # The Current Cursor Position:  17
  # Data After Modification:
  # All Students are GEMS!!!


  # Handling Binary Data:
  # It is very common requirement to read or write binary data like images,video files,audio
  # files etc.

# Q. Program to read image file and write to a new image file?

'''f1=open("rossum.jpg","rb")
f2=open("newpic.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("New Image is available with the name: newpic.jpg")'''

# Zipping and Unzipping Files:
# It is very common requirement to zip and unzip files.
# To perform zip and unzip operations, Python contains one in-bulit module zip file.
# This module contains a class : ZipFile


# To create Zip file:
# We have to create ZipFile class object with name of the zip file,mode and constant
# ZIP_DEFLATED. This constant represents we are creating zip file.
# f = ZipFile("files.zip","w","ZIP_DEFLATED")
# Once we create ZipFile object,we can add files by using write() method.
# f.write(filename)


'''from zipfile import *
f=ZipFile("file.zip",'w',ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("files.zip file created successfully")'''

# To perform unzip operation:
# We have to create ZipFile object as follows
# f = ZipFile("files.zip","r",ZIP_STORED)

# names = f.namelist()

from zipfile import *
f=ZipFile("files.zip", 'r', ZIP_STORED)
names=f.namelist()
for name in names:
   print( "File Name: ",name)
   print("The Content of this file is:")
   f1=open(name,'r')
   print(f1.read())
   print()

# Working with Directories:
# It is very common requirement to perform operations for directories like
# 1. To know current working directory
# 2. To create a new directory
# 3. To remove an existing directory
# 4. To rename a directory
# 5. To list contents of the directory

# Q1. To Know Current Working Directory:
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)
# out-Current Working Directory: /home/vishnu/Desktop/PythonTutorials/file_handling

# Q2. To create a sub directory in the current working directory:
import os
os.mkdir("hii")
print("mysub directory created in cwd")
# mysub directory created in cwd

# Q3. To create a sub directory in mysub directory:

import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")