l = [[1,2,6],[3,4,8],[5,6,8]]
r,c = 3,3
print("print first matrix:")
for i in range(r):
    for j in range(c):
        print(l[i][j],end="  ")
    print()
print("print second matrix:")
l1 = [[2,3,6],[4,3,4],[5,7,8]]
r1,c1 = 3,3
for i in range(r1):
    for j in range(c1):
        print(l1[i][j],end="  ")
    print()

# sum
l3 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(l)):
    for j in range(len(l[0])):
         l3[i][j]=l[i][j]+l1[i][j]
print("sum of two matrix:")
for i in range(r):
    for j in range(c):
        print(l3[i][j],end="  ")
    print()

    # print first matrix:
    # 1  2  6
    # 3  4  8
    # 5  6  8
    # print second matrix:
    # 2  3  6
    # 4  3  4
    # 5  7  8
    # sum of two matrix:
    # 3  5  12
    # 7  7  12
    # 10  13  16