str = input("Enter a String:")

length = len(str)

if length > 2:
    if str[-3:] == 'ing':
        str += 'ly'
    else:
        str += 'ing'
        
print(str)