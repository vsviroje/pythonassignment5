def pattern(n):
    if(n>0):
        pattern(n-1)
        print(n, end=" ")

def main():
    n=int(input("Enter Number"))
    pattern(n)
if __name__=='__main__':
    main()