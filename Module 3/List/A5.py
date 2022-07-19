def diff_var(lst):
    lst = []
    str1 = []
    for x in lst:
        if type(lst[x]) == str:
            str1.append(x)
        else:
            print()
    print(str1)


diff_var(["abc", 'dv', 'edf'])
