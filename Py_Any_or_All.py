n = int(input())
o = list(map(int,input().split()))
p = []

for j in o:
    k = str(j)
    if k == k[::-1]:
        p += [True]
    else:
        pass
if any([l==True for l in p]):
    if all([i>=0 for i in o]):
        print(True)
    else:
        print(False)
else: 
    print(False)
