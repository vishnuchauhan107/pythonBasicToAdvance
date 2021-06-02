def findPair(A, sum):
    A.sort()
    (low, high) = (0, len(A) - 1)
    while low < high:
        if A[low] + A[high] == sum:
            print("Pair found", (A[low], A[high]))

        if A[low] + A[high] < sum:
            low = low + 1
        else:
            high = high - 1
    print("Pair not found")
A = [8, 7, 2, 5, 3, 1]
sum = 10
findPair(A, sum)
print("sum is :",sum)

# out-Pair found (2, 8)
# Pair found (3, 7)
# Pair not found
# sum is : 10
'''def findpair(arr,s):
    arr.sort()
    (l,h) = (0,len(arr)-1)
    while l<h:
        if arr[l]+arr[h]==s:
            print("pair is found:",(arr[l],arr[h]))
        if arr[l]+arr[h]<s:
            l = l+1
        else:
            h = h+1
    print("pair is not found:")

arr= [8, 7, 2, 5, 3, 1]
s = 10
findpair(arr,s)'''

