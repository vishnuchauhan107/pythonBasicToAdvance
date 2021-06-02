l = eval(input(""))
r,c=list(map(int, input().split('*')))
k=0
if len(l)==r*c:
    for i in range(r):
        for j in range(c):
            print(l[k],end=" ")
            k=k+1
        print()
else:
  print(none)
'''out-[1,2,3,4,5,6]
3*2
1 2 
3 4 
5 6 
'''

