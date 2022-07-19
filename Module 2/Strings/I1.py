str1 = input("Enter first string:")
str2 = input("Enter second string:")

nstr1 = str2[:2] + str1[2:]
nstr2 = str1[:2] + str2[2:]

print(nstr1," ",nstr2)