def binary_search(arr,l,h,x):
    if h>=l:
        mid = (h+l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr, mid + 1,h, x)
    else:
      return -1
arr= [1,4,2,7,5,8,3]
arr.sort()
x =3
result = binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print("element present at index",str(result))
else:
    print("element is not present in array:")


