cases = int(input())
strs = []

for i in range(cases):
    strs.append(input())

for k in range(cases):
    evens = [v for i,v in enumerate(strs[k]) if i%2 == 0]
    odds = [v for i,v in enumerate(strs[k]) if i%2 == 1]
    print(''.join(evens), ''.join(odds))
