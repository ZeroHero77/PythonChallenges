import itertools

x = list(map(int,input().split()))
t  = list(map(int,input().split()))

try:
    for i in itertools.product(range(min(x),max(x)+1),range(min(t),max(t)+1)):
        print(i, end=' ')
except EOFError:
    pass 
