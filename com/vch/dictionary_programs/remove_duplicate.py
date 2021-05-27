d = {'h':1,'y':1,'z':2,'a':2}
d1 ={}
for k,v in d.items():
    if v not in d1.values():
        d1[k] = v
print(d1)
# out-{'h': 1, 'z': 2}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(d1)
d3.update(d2)
print(d3)
