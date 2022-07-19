def s1(lst):
    a = min(lst)
    nlst = []
    for x in lst:
        if x > a:
            nlst.append(x)

    print(min(nlst))


def s2(lst):
    lst = list(lst)
    a = min(lst)
    lst.remove(min(lst))
    print(min(lst))

s1([12, 43, 11, 32, 23, 13, 2, 1, 3, 4, 2])
s2([12, 43, 11, 32, 23, 13, 2, 1, 3, 4, 2])