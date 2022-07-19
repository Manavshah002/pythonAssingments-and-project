d1 = {"a": 200, "b": 300, "c": 200}
d2 = {"a": 100, "b": 400, "d": 100}
d3 = dict(d1)
d3.update(d2)
for a,b in d1.items():
    for x,y in d2.items():
        if a == x:
            d3[a]=(b+y)
print(d3)