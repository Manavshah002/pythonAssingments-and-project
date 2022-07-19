# Fibonacci Series

n = int(input("How many terms you want:"))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please Enter a Positive Integer:")
elif n == 1:
    print("Fibonacci Sequence upto", n, ":")
    print(n1)
    
else:
    print("Fibonacci Sequence:")
    while count < n:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1