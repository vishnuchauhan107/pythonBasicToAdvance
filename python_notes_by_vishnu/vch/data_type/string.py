# string: string is sequence of character within either single, double and triple quote.
# string item is immutable (no change)
s = 'hello'
print(s)
s = "hello"
print(s)
# accesing the character in string
#1. indexing
#2. slicing
s = "hello"
print(s[0])#out h
# and out of range index then get error

#2. slicing
s = "hello"
print(s[0::])#out hello
# if out of index then be will get empty string

s = "hello"
print(s[::-1])# out: olleh

# mathmetical operation on string
s = 'hello'
p = 'yellow'
c = s+p
print(c)# out helloyellow: both object are list then be can add
s = 'hello'
r=s*3
print(r)#hellohellohello: one object is string and second is int

#string buit in function
#1. len():to count lenght of string
s = 'hello'
print(len(s))#5

# cheaking membership:
s = 'hello'
print('h' in s)#true
print('t' not in s)#true

# comparision of string
# we can use comparison operator (<,>,<=,>=)
s = 'hello'
t = 'hello'
print(s==t)#true
print(s!=t)#false

#removing space from the string:
#1.rstrip()== to remove space at right sight
#2.lstrip()== to remove space at left sight
#3.strip()== to remove all space both side
s = 'hello  '
m =s.lstrip()
print(m==s)#true


# finding substring in the string
# to method are available 1.find:2.index()
#1.find():return the first occurence of the given substring if it is not available then get -1
s = 'hello'
print(s.find('l'))#2
print(s.find('m'))#-1
print(s.rfind('l'))#3

#2.index():return the first occurence of the given string substring if it is not available then be will get error
s ='hello'
print(s.index('l'))#2

# counting substring in the given string
# 1.count(): it will search through out the string
s = "abababababnsnsvadbsj"
print(s.count('a'))#6
print(s.count('ab'))#5
print(s.count('a',0,1))#1


#replacing a string with another string:
#s.replace(old,new)
s = 'string'
s1 = s.replace('string','hello')
print(s1)#hello

#splitting of string:
#l=s.split(seperator):the defoult seperator is space the type of split() method is list
s='hello'
l = s.split()
print(l)#out ['hello']

s = "7-5-21"
l = s.split('-')
print(l)#['7', '5', '21']

#joining of string:we can join a group of string wrt the given seperator.
s = "hello"
t = '-'.join(s)
print(t)#h-e-l-l-o

# changing case of string:
'''
1.upper():to convert all character in upper case 
2. lower():to convert all charactern inn lower case
3.swapecase ():to covert all lower to upper and upper to lower 
4.title():to covert all character to title case 
5.capitalize():to convert first character wiil be upper case 
'''
s = "My name Is Vishnu CHAUHAN"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
# out MY NAME IS VISHNU CHAUHAN
# my name is vishnu chauhan
# My Name Is Vishnu Chauhan
# My name is vishnu chauhan


# to cheak type of character print in a string:
'''
1.isalnum()
2.isalpha()
3.isdigit()
4.islower()
5.isupper()
6.istitle()
7.isspace()
'''
print("hello254".isalnum())
print("hello".isalpha())
print("254".isdigit())
print("hello254".islower())
print("Hello254".istitle())
print(" ".isspace())
# out:True
# True
# True
# True
# True
# True