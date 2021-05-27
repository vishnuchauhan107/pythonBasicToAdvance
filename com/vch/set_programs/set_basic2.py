s={'have','a','good','day','xyz','pqr'}
s1 = {'a','e','i','o','u'}
s3 = set()
for i in s:
    for j  in s1:
        if j in i:
           s3.add(i)
print(s3)
# out-{'day', 'have', 'a', 'good'}
