d1 = {'a': 12, 'b': 33, 'c': 12, 'd': 2, 'e': 3, 'f': 4, 'g': 33}
t1 =[]

for x in d1.values():
    t1.append(x)
print(set(t1))