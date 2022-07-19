str = input("Enter a string:")

length = len(str)

if length > 1:
    str = str[:2] + str[-2:]
    print(str)
    
else:
    print("Empty String")
    