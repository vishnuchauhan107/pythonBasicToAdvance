lst = eval(input("enter the list:"))
r = int(input("enter the row:"))
c = int(input("enter the colum:"))
index = 0
l = index
if r*c == len(lst):
 for i in range(3):
    for j in range(2):
        print(lst[index],end=" ")
        index = index+1
    print()
else:
    print("none")
# enter the list:[1,2,3,4,5,6]
# enter the row3
# enter the colum2
# 1 2
# 3 4
# 5 6
# enter the list:[1,2,3]
# enter the row:2
# enter the colum:5
# none
