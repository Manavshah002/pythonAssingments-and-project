def checkrange(num):
    if num in range(1,10):
        print(f"{num} is in given range")
    else:
        print(f"{num} is out of given range")
        

num = int(input("Enter a number: "))
checkrange(num)