str = input("Enter a String:")

temp = str[0]
print(str)
str = str.replace(temp, '$')
str = temp + str[1:]
print(str)