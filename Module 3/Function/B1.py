def factorial(num):
    fact = 1

    if num < 0:
        print("Factorail of negative number doesn't exist")
    elif num == 0:
        print("The Factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            fact = fact*i
            
    print("The Factorial of", num, "is", fact)


num = int(input("Enter a number: "))
factorial(num)