import re
n = int(input())

def loopai(n):
    x = [i+1 for i in range(n)]
    z = x
    print(re.sub(' ','',re.sub('\,','',re.sub('\]','',re.sub('\[','',str(z))))))

def main():
    loopai(n)


if __name__ == '__main__':
    main()
