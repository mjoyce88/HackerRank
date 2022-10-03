tp, name, phone = dict(), str(), ""
for i in range(int(input())):
    name, phone = input().split()
    tp[name]=phone
while(True):
    try:
        name = input()
        if name in tp: print(name+"="+tp[name])
        else: print("Not found")
    except EOFError:
        break;
