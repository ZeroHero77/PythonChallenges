import itertools, re  
 
k = [] 
n = input().split()

for i in itertools.permutations(n[0],int(n[1])):
    j = str(i).replace("(", "").replace(")","").replace("\'","").replace(",","").replace(" ","")
    k += [j]
l = sorted(k)
for i2 in l:
    print(i2)
