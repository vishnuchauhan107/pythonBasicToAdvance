'''
Dictionary Data Structure:
We can use List,Tuple and Set to represent a group of individual objects as a single entity.
If we want to represent a group of objects as key-value pairs then we should go for
Dictionary.
Duplicate keys are not allowed but values can be duplicated.
Hetrogeneous objects are allowed for both key and values.
insertion order is not preserved
Dictionaries are mutable
Dictionaries are dynamic
indexing and slicing concepts are not applicable
'''
# How to create Dictionary?
d={}
d[100]="durga"
d[200]="ravi"
d[300]="shiva"
print(d)
# out-{100: 'durga', 200: 'ravi', 300: 'shiva'}

# How to access data from the dictionary?
# We can access data by using keys.
d={100:'durga' ,200:'ravi', 300:'shiva'}
print(d[100]) #durga
print(d[300]) #shiva

# How to delete elements from dictionary?
# del d[key]
d={100:"durga",200:"ravi",300:"shiva"}
print(d)
del d[100]
print(d)
# {200: 'ravi', 300: 'shiva'}

# d.clear()
# To remove all entries from the dictionary

d={100:"durga",200:"ravi",300:"shiva"}
print(d)
d.clear()
print(d)
# out-{100: 'durga', 200: 'ravi', 300: 'shiva'}
# {}


# Important functions of dictionary:
# 1. dict():
# To create a dictionary

d=dict()# {}
d=dict({100:"durga",200:"ravi"})
print(d)
# out-{100: 'durga', 200: 'ravi'}

# 2. len()
# Returns the number of items in the dictionary
# 3. clear():
# To remove all elements from the dictionary
# 4. get():
# To get the value associated with the key
# d.get(key)
# If the key is available then returns the corresponding value otherwise returns None.It
# wont raise any error.
# d.get(key,defaultvalue)
# If the key is available then returns the corresponding value otherwise returns default
# value.
d={100:"durga",200:"ravi",300:"shiva"}
print(d.get(100)) #durga
print(d.get(400)) #None
print(d.get(100,"Guest")) #durga
print(d.get(400,"Guest")) #Guest

# 3. pop():
# d.pop(key)
# It removes the entry associated with the specified key and returns the corresponding
d={100:"durga",200:"ravi",300:"shiva"}
print(d.pop(100))
print(d)
# out-{200: 'ravi', 300: 'shiva'}


# 4. popitem():
# It removes an arbitrary item(key-value) from the dictionaty and returns it.
d={100:"durga",200:"ravi",300:"shiva"}
print(d)
print(d.popitem())
print(d)
# out-{100: 'durga', 200: 'ravi', 300: 'shiva'}
# (300, 'shiva')
# {100: 'durga', 200: 'ravi'}

# 5. keys():
# It returns all keys associated eith dictionary

d={100:"durga",200:"ravi",300:"shiva"}
print(d.keys())
for k in d.keys():
  print(k)

  # dict_keys([100, 200, 300])
  # 100
  # 200
  # 300

  # 6. values():
  # It returns all values
  # 6
  # associated with the dictionary

d={100:"durga",200:"ravi",300:"shiva"}
print(d.values())
for v in d.values():
   print(v)
   # dict_values(['durga', 'ravi', 'shiva'])
   # durga
   # ravi
   # shiva

# 7. items():
# It returns list of tuples representing key-value pairs.
# [(k,v),(k,v),(k,v)]

d={100:"durga",200:"ravi",300:"shiva"}
for k,v in d.items():
  print(k,"--",v)

# out-100 -- durga
# 200 -- ravi
# 300 -- shiva

# 8. copy():
# To create exactly duplicate dictionary(cloned copy)
# d1=d.copy();

# 9. setdefault():
# d.setdefault(k,v)
# If the key is already available then this function returns the corresponding value.
# If the key is not available then the specified key-value will be added as new item to the
# dictionary

d={100:"vishnu",200:"ravi",300:"shiva"}
print(d.setdefault(400,"pavan"))
print(d)
print(d.setdefault(100,"sachin"))
print(d)
# out- pavan
# {100: 'vishnu', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
# vishnu
# {100: 'vishnu', 200: 'ravi', 300: 'shiva', 400: 'pavan'}


# 10. update():
# d.update(x)
# All items present in the dictionary x will be added to dictionary d

d={'A':100,'B':200,'C':300}
s=sum(d.values())
print("Sum= ",s)
# out-Sum=  600







