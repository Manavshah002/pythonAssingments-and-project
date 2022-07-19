str = '''He had died by the time I read that passage in one of his books, 
         so I couldn't write him, as is my normal practice when an author's words puzzle me.'''
# str = input("Enter a String:")
 
count = dict()
word = str.split()

for i in word:
    
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)