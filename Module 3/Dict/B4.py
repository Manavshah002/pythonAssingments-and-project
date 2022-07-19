d = {'a':3,'d':4,'b':1,'c':2}

sort = sorted((value, key) for (key, value) in d.items())
print(sort)
sort.reverse()
print(sort)