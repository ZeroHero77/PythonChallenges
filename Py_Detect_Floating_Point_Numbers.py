import re 
x = int(input())

for i in range(x):
    k = input()
    if re.search(r'^[+-]?[0-9]*[.][0-9]+$',k):
        print(True)
    else:
        print(False)
