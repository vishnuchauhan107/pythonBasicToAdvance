def linear_search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = linear_search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
    # out-Element is present at index 3

