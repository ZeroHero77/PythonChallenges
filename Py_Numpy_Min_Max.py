import numpy

a =  numpy.array(input().split())
x = int(a[0])
k = int(a[1])
o = []

for i in range(x):
    j = numpy.array(input().split())
    m = int(j[0])
    n = int(j[1])
    
    if m < n:
        o += [m]
    else:
        o += [n]
print(numpy.max(o))
