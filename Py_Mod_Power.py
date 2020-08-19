x = int(input())
k = int(input())
b = int(input())

def main():
    moderpow(x,k,b)

def moderpow(x,k,b):
    print(x**k)
    print(x**k%b)

if __name__ == '__main__':
    main()
