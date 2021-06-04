def leftRotate(arr, n, k):
    for i in range(k, k + n):
        print((arr[i % n]),
              end=" ")


arr = [1, 3, 5, 7, 9,10]
n = len(arr)
k = 4;
leftRotate(arr, n, k)
print()
# out-9 10 1 3 5 7

k = 2;
leftRotate(arr, n, k)
print()
# out-5 7 9 10 1 3
k = 14;
leftRotate(arr, n, k)
print()
# out-5 7 9 10 1 3
k = 3;
leftRotate(arr, n, k)
print()
# out-7 9 10 1 3 5
