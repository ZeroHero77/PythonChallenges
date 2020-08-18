import numpy as np;

np.set_printoptions(sign=' ')

STDIN = np.array(input().split(),float)


b = np.floor(STDIN)
c = np.ceil(STDIN)
d = np.rint(STDIN)

print(b)
print(c)
print(d)