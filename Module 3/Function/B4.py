def palindrome(str1):
    str2 = str1[::-1]
    if str1 == str2:
        print(f"{str1} is palindrome")
    else:
        print(f"{str1} is not palindrome")
        

palindrome('mam')
palindrome('gopan')