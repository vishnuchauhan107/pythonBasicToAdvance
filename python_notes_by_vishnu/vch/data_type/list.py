'''
python list: list is a collection of data structure of sequence item
'''
#how to initialize the list
list = ['1','3','5']
print(list)
#accessing the list element:
#1.by indexing
#2.by slicing
# indexing

list = ['1','3','5']
re= list[0]#out1 if out of index then be will get error
print(re)
#slicing
list = ['1','3','5', 'hello']
re = list[::-1]#reverse list
me = list[::]# output is same list
print(re)
print(me)
# if in slicing the indexing error then we found empty list no error
#list method ()
# list is mutable
list = ['1','3','5']
list[0]='hello'
print(list)# out ['hello', '3','5',]
#1.append
list =['3','5']
list.append(10)
list.append(50)
print(list)
#extrend method: add the list or iterable item in a current list
list = ['1','3','5']
list.extend([7,8,9])
print(list)
# if we pass extend(9) then we will get error becouse int object are not iterable


#3. insert : add the element at position
list = ['1','3','5', 'hello']
list.insert(0,'python')
print(list)

#4. clear: remove all item in a list
list = ['1','3','5', 'hello']
list.clear()
print(list)

#5. pop():remove the element at specified value
list = ['1','3','5', 'hello']
re = list.pop()
print(list)# if a i can use pop function without any arguments then last element is remove
re = list.pop(2)# out ['1','3'] if out of index then we will get error
print(list)


#6.remove:remove the element the specified value
list = ['1','3','5', 'hello']
list.remove('3')
print(list)

#7. index(): return the endex of element and return the argument
list = ['1','3','5', 'hello']
re = list.index('3')
print(re)

#8 count(): count the frequency of the element
list = ['1','3','5', 'hello','5']
re = list.count('5')# if specified element is not present then return 0
print(re)

#9.sort: sort the element in given list
list = ['1','3','5', 'hello','2']
list.sort()
print(list)

list = ['ravi', 'vishnu', 'kunal','sumit']
list.sort()
print(list)

#10. reverse():reverse the list
list = ['1','3','5', 'hello']
list.reverse()
print(list)

#11.copy: return the copy of the list
list = ['1','3','5', 'hello']
list2= list.copy()
print(list)
print(list2)
#sort the list with item lenght
list = ['1','3','5','2', 'hello']
list.sort()
print(list)

#del statement (del not a method of list)
list = ['1','3','5', 'hello']
del list[0]
print(list)

# len(): return the lenght of
list = ['1','3','5', 'hello']
print(len(list))