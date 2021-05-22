# If we want to represent a group of Strings according to a particular format/pattern then we
# should go for Regular Expressions.
# We can develop Regular Expression Based applications by using python module: re
# This module contains several inbuilt functions to use Regular Expressions very easily in our
# applications.


# 1. compile()
# re module contains compile() function to compile a pattern into RegexObject.
# pattern = re.compile("ab")

# 2. finditer():
# Returns an Iterator object which yields Match object for every Match
# matcher = pattern.finditer("abaababa")

# On Match object we can call the following methods.
# 1. start()  Returns start index of the match
# 2. end()  Returns end+1 index of the match
# 3. group()  Returns the matched string

import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababa")
for match in matcher:
  count+=1
  print(match.start(),"...",match.end(),"...",match.group())
print("The number of occurrences: ",count)
# out-0 ... 2 ... ab
# 3 ... 5 ... ab
# 5 ... 7 ... ab
# The number of occurrences:  3
import re
count=0
matcher=re.finditer("ab","abaababa")
for match in matcher:
  count+=1
  print(match.start(),"...",match.end(),"...",match.group())
print("The number of occurrences: ",count)
# out-0 ... 2 ... ab
# 3 ... 5 ... ab
# 5 ... 7 ... ab
# The number of occurrences:  3

# Character classes:
# We can use character classes to search a group of characters
# 1. [abc]===>Either a or b or c
# 2. [^abc] ===>Except a and b and c
# 3. [a-z]==>Any Lower case alphabet symbol
# 4. [A-Z]===>Any upper case alphabet symbol
# 5. [a-zA-Z]==>Any alphabet symbol
# 6. [0-9] Any digit from 0 to 9
# 7. [a-zA-Z0-9]==>Any alphanumeric character
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)


import re
matcher=re.finditer("x","a7b@k9z")
for match in matcher:
   print(match.start(),"......",match.group())

# out-x = [abc]
# 0 ...... a
# 2 ...... b
# x = [^abc]
# 1 ...... 7
# 3 ...... @
# 4 ...... k
# 5 ...... 9
# 6 ...... z
# x = [a-z]
# 0 ...... a
# 2 ...... b
# 4 ...... k
# 6 ...... z
# x = [0-9]
# 1 ...... 7
# 5 ...... 9
# x = [a-zA-Z0-9]
# 0 ...... a
# 1 ...... 7
# 2 ...... b
# 4 ...... k
# 5 ...... 9
# 6 ...... z
# x = [^a-zA-Z0-9]
# 3 ...... @

# Pre defined Character classes:
# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .  Any character including special characters

import re
matcher=re.finditer("x","a7b k@9z")
for match in matcher:
   print(match.start(),"......",match.group())
   # out-x = \s:
   # 3 ......
   # x = \S:
   # 0 ...... a
   # 1 ...... 7
   # 2 ...... b
   # 4 ...... k
   # 5 ...... @
   # 6 ...... 9
   # 7 ...... z
   # x = \d:
   # 1 ...... 7
   # 6 ...... 9
   # x = \D:
   # 0 ...... a
   # 2 ...... b
   # 3 ......
   # 4 ...... k
   # 5 ...... @
   # 7 ...... z
   # x = \w:
   # 0 ...... a
   # 1 ...... 7
   # 2 ...... b
   # 4 ...... k
   # 6 ...... 9
   # 7 ...... z
   # x = \W:
   # 3 ......
   # 5 ...... @
   # x = .
   # 0 ...... a
   # 1 ...... 7
   # 2 ...... b
   # 3 ......
   # 4 ...... k
   # 5 ...... @
   # 6 ...... 9
   # 7 ...... z

# Qunatifiers:
# We can use quantifiers to specify the number of occurrences to match.
# a  Exactly one 'a'
# a+  Atleast one 'a'
# a*  Any number of a's including zero number
# a?  Atmost one 'a' ie either zero number or one number
# a{m}  Exactly m number of a's
# a{m,n}  Minimum m number of a's and Maximum n number of a's

import re
matcher=re.finditer("x","abaabaaab")
for match in matcher:
  print(match.start(),"......",match.group())
  # out if-x = a:
  # 0 ...... a
  # 2 ...... a
  # 3 ...... a
  # 5 ...... a
  # 6 ...... a
  # 7 ...... a
  # x = a+:
  # 0 ...... a
  # 2 ...... aa
  # 5 ...... aaa
  # x = a*:
  # 0 ...... a
  # 1 ......
  # 2 ...... aa
  # 4 ......
  # 5 ...... aaa
  # 8 ......
  # 9 ......
  # 5
  # x = a?:
  # 0 ...... a
  # 1 ......
  # 2 ...... a
  # 3 ...... a
  # 4 ......
  # 5 ...... a
  # 6 ...... a
  # 7 ...... a
  # 8 ......
  # 9 ......
  # x = a{3}:
  # 5 ...... aaa
  # x = a{2,4}:
  # 2 ...... aa
  # 5 ...... aaa

# Important functions of re module:
# 1. match()
# 2. fullmatch()
# 3. search()
# 4.findall()
# 5.finditer()
# 6. sub()
# 7.subn()
# 8. split()
# 9. compile()

# 1. match():
# We can use match function to check the given pattern at beginning of target string.
# If the match is available then we will get Match object, otherwise we will get None.

''''import re
s=input("Enter pattern to check: ")
m=re.match(s,"abcabdefg")
if m!= None:
  print("Match is available at the beginning of the String")
  print("Start Index:",m.start(), "and End Index:",m.end())
else:
  print("Match is not available at the beginning of the String")
# out-else:
# 8)
# print("Match is not available at the beginning of the String")
'''
# 2. fullmatch():
# We can use fullmatch() function to match a pattern to all of target string. i.e complete string
# should be matched according to given pattern

'''import re
s=input("Enter pattern to check: ")
m=re.fullmatch(s,"ababab")
if m!= None:
   print("Full String Matched")
else:
   print("Full String not Matched")
   # out-he number of occurrences:  3
   # Enter pattern to check: ababab
   # Full String Matched'''


# 3. search():
# We can use search() function to search the given pattern in the target string.
# If the match is available then it returns the Match object which represents first occurrence of the
# match

'''import re
s=input("Enter pattern to check: ")
m=re.search(s,"abaaaba")
if m!= None:
  print("Match is available")
  print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
else:
  print("Match is not available")
  # out-Enter pattern to check: aaa
  # Match is available
  # First Occurrence of match with start index: 2 and end index: 5'''


# 4. findall():
# To find all occurrences of the match.
# This function returns a list object which contains all occurrences.
import re
l=re.findall("[0-9]","a7b9c5kz")
print(l)
# out-['7', '9', '5']


# 5. finditer():
# Returns the iterator yielding a match object for each match.
# On each match object we can call start(), end() and group() functions.
import re
itr=re.finditer("[a-z]","a7b9c5k8z")
for m in itr:
  print(m.start(),"...",m.end(),"...",m.group())
  # out-0 ... 1 ... a
  # 2 ... 3 ... b
  # 4 ... 5 ... c
  # 6 ... 7 ... k
  # 8 ... 9 ... z

# 6. sub():
# sub means substitution or replacement
# re.sub(regex,replacement,targetstring)
import re
s=re.sub("[a-z]","#","a7b9c5k8z")
print(s)
# out-#7#9#5#8#

# 7. subn():
# It is exactly same as sub except it can also returns the number of replacements.
# This function returns a tuple where first element is result string and second element is number of
# replacements.
# (resultstring, number of replacements)

import re
t=re.subn("[a-z]","#","a7b9c5k8z")
print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])
# out-The Result String: #7#9#5#8#
# The number of replacements: 5


# 8. split():
# If we want to split the given target string according to a particular pattern then we should go for
# split() function
import re
l=re.split(",","sunny,bunny,chinny,vinny,pinny")
print(l)
for t in l:
  print(t)
  # out-['sunny', 'bunny', 'chinny', 'vinny', 'pinny']
  # sunny
  # bunny
  # chinny
  # vinny
  # pinny

  # ^ symbol:
  # We can use ^ symbol to check whether the given target string starts with our provided pattern or
  # not.
import re
s="Learning Python is Very Easy"
res=re.search("^Learn",s)
if res != None:
   print("Target String starts with Learn")
else:
   print("Target String Not starts with Learn")
   # out-Target String starts with Learn

# $ symbol:
# We can use $ symbol to check whether the given target string ends with our provided pattern or
# not
import re
s="Learning Python is Very Easy"
res=re.search("Easy$",s)
if res != None:
  print("Target String ends with Easy")
else:
  print("Target String Not ends with Easy")
  # out-Target String ends with Easy

# f we want to ignore case then we have to pass 3rd argument re.IGNORECASE for search()
# function.
# Eg: res = re.search("easy$",s,re.IGNORECASE)
import re
s="Learning Python is Very Easy"
res=re.search("easy$",s,re.IGNORECASE)
if res != None:
   print("Target String ends with Easy by ignoring case")
else:
   print("Target String Not ends with Easy by ignoring case")
   # out-Target String ends with Easy by ignoring case
   