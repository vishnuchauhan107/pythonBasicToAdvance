s = set([5, 10, 3, 15, 2, 20])
sum = max(s)+min(s)
print(sum)
# out-22
set1={4,7,10,5,1}
set2={4,10,2,6,1,9}
set3 = set2-set1
set4 = set()
for i in set3:
    if i%2==0:
        set4.add(i)
print(set4)
# out-{2, 6}

