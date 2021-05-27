def fib():
  a,b=0,1
  while True:
     yield a
     a,b=b,a+b
for f in fib():
  if f>10:
    break
  print(f,end = ",")
  # out-0,1,1,2,3,5,8,
