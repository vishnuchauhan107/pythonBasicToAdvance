#tuple data type:
'''tuple is a collection of immutable collection of objects once be creat tuple objects we
 can not change any objects
 insertion order is preserved
 heterogeneous objects are allowed
 '''
t = 1,2,3,4
print(t)
print(type(t))
#out-(1, 2, 3, 4)
#<class 'tuple'>

t=()#empty tuple
t = 10,
print(t,type(t))#(10,) <class 'tuple'>

#list to tuple

lst=[1,2,3,4]
t = tuple(lst)
print(t)# out(1, 2, 3, 4)


t= tuple(range(10,20,2))
print(t)#out:(10, 12, 14, 16, 18)


#accesing elements of tuple :
#1. by index
#2.by slicing
t = (10, 12, 14, 16, 18)
print(t[0])#10
print(t[3])#16
#print(t[100]) indexerror

t = (10, 12, 14, 16, 18)
print(t[0::])
print(t[::-1])
print(t[::2])
#out-(10, 12, 14, 16, 18)
#(18, 16, 14, 12, 10)
#(10, 14, 18)

#tuple vs immutability
#t=(10, 12, 14, 16, 18)
#t[1]=12
#print(t) out type error becouse tuple object does no t not support item assingment

# mathmetical operation for tuple
t=(10, 12, 14, 16, 18)
t1=(0, 2, 1, 1, 6)
t2= t+t1
print(t2)#(10, 12, 14, 16, 18, 0, 2, 1, 1, 6)

t=(10, 12, 14, 16, 18)
t1=t*3
print(t1)#(10, 12, 14, 16, 18, 10, 12, 14, 16, 18, 10, 12, 14, 16, 18)

#len():to count the lenght of tuple

t=(10, 12, 14, 16, 18)
print(len(t))#5

# count(): to count number of occurence of given element in tuple
t=(10,10,5,12, 12, 14, 16, 18)
c= t.count(10)
print(c)#2

#. index():return the index of first occurence of given element if element is not found then be will get value error
t=(10, 12, 14, 16, 18)
i = t.index(10)
print(i)

#.sorted(): to sorted the given elements on defoult its natural sorting order

t=(10,10,5,12, 12, 14, 16, 18)
t1 = sorted(t)
print(t1)#[10, 12, 13, 14, 16, 18, 30, 88]
t1 = sorted(t,reverse=True)
print(t1)#out-[88, 30, 18, 16, 14, 13, 12, 10]

# min() and max() function:these function return min and max value according to its defoult natural order

t=(10,10,5,12, 12, 14, 16, 18)
print(min(t))
print(max(t))
# out-5
# 18
'''#. cmp(): it is compare the element of both tuples :
# if both tuples are eqal then return 0
if first is less then second themn return -1 
if first tupke ids greater then second then return +1

t1 =(1,2,5,3,4)
t2= (2,3,45,2)
t1 =(1,2,5,3,4)
print(cmp(t1,t2)) cmp function is availale in python2 not python 3

'''
# tuple packing and and unpacking
a=2
b=6
c=9
d=8
t= a,b,c,d
print(t)# out(2, 6, 9, 8)


'''tuple comprehension:
'''
t = (x**2 for x in range(1,6))
print(t)
# out-(2, 6, 9, 8)
# <generator object <genexpr> at 0x7f5d194bec10>
