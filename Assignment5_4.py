
def SumOfDigit(n):
    s=0
    if n != 0:
        s = SumOfDigit(int(n/10))
    return s+int(n % 10)


def main():
    n=int(input("Enter Number"))
    print(SumOfDigit(n))


if __name__ == '__main__':
    main();