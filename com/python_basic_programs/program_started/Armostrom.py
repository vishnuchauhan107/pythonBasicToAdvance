n = int(input("Enter the number:"))
sum = 0
num = n
while num>=1:
    re = num%10
    sum = sum+re**3
    num = num//10
if n==sum:
  print(n,"is armostrom number")
else:
  print(n,"not armostrom number")
# Enter the number:407
# 407 is armostrom number
# Enter the number:153
# 153 is armostrom number
# Enter the number:20
# 20 not armostrom number
