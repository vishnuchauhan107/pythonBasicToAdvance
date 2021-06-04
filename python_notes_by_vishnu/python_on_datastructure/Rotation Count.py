def Rotation_Count(arr,n):
    min = arr[0]
    for i in range(0,n):
        if min>arr[i]:
            min = arr[i]
            min_index = i
    return min_index
arr = [15, 11, 12, 3, 6, 12]
n = len(arr)
print(Rotation_Count(arr, n))

# out-3
