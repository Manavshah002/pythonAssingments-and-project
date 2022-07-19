def exist(d,x):
    if x in d:
        print("Key is Exist")
    else:
        print("Key don't Exist")

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}        
exist(d, 2)
exist(d, 10)
