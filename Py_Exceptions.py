n = int(input())

for i in range(n):
    k,j = input().split()
    try:
        if int(k) >0 and int(j) >0:
            print(int(int(k)/int(j)))
        else:    
            print(int(int(k)%int(j)))
    except Exception as e:
        print('Error Code:',e)
