# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int,input().split()))
x = a[0]
k = a[1]
b = input()

def main():
    polynomio(b,k)

def polynomio(b,k):
    if eval(b) == k:
        print(True)
    else: 
        print(False)

if __name__=='__main__': main() 
