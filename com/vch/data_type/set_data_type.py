'''
if we want to represent a group of unique values as a single entity then we should go for set
in set duplicate are not allowed
and indexing and slicing is not allowed
and and tuple is mutable
we can represent set in {}
'''
# Creation of Set objects
s={10,20,30,40}
print(s)
print(type(s))
# {40, 10, 20, 30}
# <class 'set'>

s=set()
print(s)
print(type(s))
# set()
# <class 'set'>
# Process finished with exit code 0

# Important functions of set:
# 1. add(x):
# Adds item x to the set-
s={10,20,30}
s.add(40)
print(s) #{40, 10, 20, 30}

# 2. update(x,y,z):
# To add multiple items to the set.-
s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)
# out-{0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}


# 3. copy():
# Returns copy of the set.
# It is cloned object.-

s={10,20,30}
s1=s.copy()
print(s1)
# {10, 20, 30}

# 4. pop():
# It removes and returns some random element from the set-

s={40,10,30,20}
print(s)
print(s.pop())
print(s)
# out-{10, 20, 30}

# 5. remove(x):
# It removes specified element from the set.
# If the specified element not present in the Set then we will get KeyError

s={40,10,30,20}
s.remove(30)
print(s)# {40, 10, 20}

# 6. discard(x):
# It removes the specified element from the set.
# If the specified element not present in the set then we won't get any error.

s={10,20,30}
s.discard(10)
print(s)
s.discard(50)
print(s)
# {20, 30}
# {20, 30}

# 7.clear():
# To remove all elements from the Set.-
s={10,20,30}
print(s)
s.clear()
print(s)
# set()

# Mathematical operations on the Set:
# 1.union():
# x.union(y) ==>We can use this function to return all elements present in both sets
# x.union(y) or
# x|y

x={10,20,30,40}
y={30,40,50,60}
print(x.union(y)) #{10, 20, 30, 40, 50, 60}
print(x|y)
#{10, 20, 30, 40, 50, 60}

# 2. intersection():
# x.intersection(y) or x&y
# Returns common elements present in both x and y

x={10,20,30,40}
y={30,40,50,60}
print(x.intersection(y))#{40,30}
print(x&y)
#{40, 30}



# 3. difference():
# x.difference(y) or x-y
# returns the elements present in x but not in y

x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y)) #{10, 20}
print(x-y)
#{10, 20}
print(y-x)
#{50, 60}



# 4.symmetric_difference():
# x.symmetric_difference(y) or x^y
# Returns elements present in either x or y but not in both


x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)
#{10, 50, 20, 60}
#{10, 50, 20, 60}

# Membership operators: (in , not in)

s=set("durga")
print(s)
print('d' in s)
print('z' in s)

# out- {'g', 'a', 'd', 'u', 'r'}
# True
# False

# Set Comprehension:
# Set comprehension is possible

s={x*x for x in range(5)}
print(s) #{0, 1, 4, 9, 16}

s={2**x for x in range(2,10,2)}
print(s)
#{16, 256, 64, 4}