def square():
    lst = []
    for x in range(1,31):
        lst.append(x**2)
    print(lst[:5])
    print(lst[-5:])

square()