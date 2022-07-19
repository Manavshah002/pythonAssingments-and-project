def count(str):
    c = 0
    for x in str:
        if len(x) > 1 and x[0] == x[-1]:
            c += 1
    print(c)


count(["aba", "abc", "dhd"])