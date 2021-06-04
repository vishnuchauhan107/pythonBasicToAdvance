def area_perimeter(l,b):

    return l*b,2*(l+b)



l = int(input("enter the lenght:"))
b = int(input("enter the breathe:"))
A,P = area_perimeter(l,b)
print("area = ",A,"perimeter=",P)
# out-enter the lenght:5
# enter the breathe:6
# area =  30 perimeter= 22
