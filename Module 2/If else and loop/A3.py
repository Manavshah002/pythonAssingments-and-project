
a, b, c = input("ENTER THE VALUE:").split()

a = int(a)
b = int(b)
c = int(c)

if a == b or b == c or c == a:
    sum = 0
else:
    sum = a + b + c

print(sum)