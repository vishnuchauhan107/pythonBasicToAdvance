def binarysearch(arr,key):
    l = 0
    h = len(arr)-1
    f = False
    while l<=h and not f:
        mid = (l+h)//2
        if key==arr[mid]:
            f = True
        elif key>arr[mid] :
           l = mid+1
        else:
            h = mid-1
    if f == True:
       print("key is found",)
    else:
       print("key is not found")
arr = [23,1,4,2,3]
arr.sort()
print(arr)
key =3
v= binarysearch(arr,3)
print(v)