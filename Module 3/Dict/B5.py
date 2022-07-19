d1 = {"a":1,"b":3}
d2 = {"c":3,"d":4}
d3 ={}

for x in (d1,d2):
    d3.update(x)
    
print(d3) 