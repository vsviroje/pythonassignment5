def pattern(n):
    if(n>0):
        print("*",end=" ")
        pattern(n-1)

def main():
    n=int(input("Enter Number"))
    pattern(n)
if __name__=='__main__':
    main()