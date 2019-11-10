
def factorial(n):
    s = 1
    if n != 0:
        s = factorial(n-1)
        return s*n
    else:
        return 1


def main():
    n=int(input("Enter Number"))
    print(factorial(n))


if __name__ == '__main__':
    main();