n = 0
n = int(input())
d = dict(input().split() for x in range(n))
for i in range(n):
    c = input()
    t = d.get(c)

    if t == None:
        print("Not found")
    else:
        print(c + "=" + t)
