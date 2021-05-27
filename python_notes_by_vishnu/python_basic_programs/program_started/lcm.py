def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
def lcmm(x, y):
   lcm = (x*y)//hcf(x,y)
   return lcm
num1 = 54
num2 = 24
print("The L.C.M. is", lcmm(num1, num2))
# out-The L.C.M. is 216
