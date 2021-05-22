# nested list
list = ['1','3','5', 'hello',['2','8']]
print(list)
print(list[4][1])# out 8

list=[[1,2,3],[4,5,6],[3,4,1]]
print(list)
for i in list:
    print(i)
print("element matrix type")
for i in range(len(list)):
   for j in range(len(list[i])):
      print(list[i][j],end=' ')
   print()
   # out element matrix type
   # 1 2 3
   # 4 5 6
   # 3 4 1

# list coprehension:
# syntax: list[expression for item in list if condition]
list = [x*x for x in range(1,11)]
print(list)
# out [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [2*x for x in range(1,11)]
print(list)
# out:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
list2 =[x for x in range(1,30) if x%2==0]
print(list2)
#out:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

list = ['vishnu', 'chauhan', 'thakur', 'rajput']
l = [m[0] for m in list]
print(l)
#out['v', 'c', 't', 'r']
list1= [1,2,3,4]
list2= [5,6,7,8]
list3=[i for i in list1 if i not in list2]
print(list3)
#out:[1, 2, 3, 4]
list3=[i for i in list1 if i in list2]
print(list3)
#out:[]
