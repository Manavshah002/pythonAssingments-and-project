from collections import Counter
lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in lst:
    result[d['item']] += d['amount']
print(result) 