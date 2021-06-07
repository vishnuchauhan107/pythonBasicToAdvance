n = int(input())
l = set(map(int, input().split()))
q = int(input())
for i in range(q):
    m = int(input())
    c = 0
    for j in l:
        if m > j:
            c = c + 1
    print(c)


