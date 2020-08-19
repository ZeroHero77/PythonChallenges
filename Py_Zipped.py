x,k = list(map(int,input().split()))
#x = a[0]
#k = a[1] 

sheet = []

try: 
    for i in range(x):
        
        a = list(map(float,input().split()))
        
        sheet.append(a)
     
except EOFError:
    pass

for j in zip(*sheet):
    print(sum(j)/k)
