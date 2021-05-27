def calculator(x,y):
    sum = x+y
    mul = x*y
    sub = x-y
    div = x/y
    return sum,mul,sub,div
a = calculator(3,1)
for i in a:
    print(i)
    # out-4
    # 3
    # 2
    # 3.0
    