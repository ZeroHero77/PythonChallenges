x = int(input())
k = int(input())

def main():
    divmodio(x,k)

def divmodio(x,k):
    print(x//k)
    print(x%k)
    print(divmod(x,k))

if __name__ == '__main__':
    main()
