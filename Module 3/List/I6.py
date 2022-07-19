def unique_list(lst):
    final = []
    for x1 in lst:
        if x1 not in final:
            final.append(x1)
    print(final)

unique_list([2, 4, 5, 2, 3, 5, 2, 7])
