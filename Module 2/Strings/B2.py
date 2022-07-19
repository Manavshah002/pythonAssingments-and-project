str = input("Enter a String:")
 
freq = {}
for i in str:
    key = freq.keys()
    if i in key:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)