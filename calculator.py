def main():
    x = int(input("What is x: "))
    y = int(input("What is y: "))
    added(x, y)
    divi(x, y)
    mod(x, y)
    multi(x, y)
    sub(x, y)


def added(x, y):
    print(x)
    print(y)
    print(f"{x+y}\n")


def divi(x, y):
    print(x)
    print(y)
    print(f"{x/y}\n")


def mod(x, y):
    print(x)
    print(y)
    print(f"{x%y}\n")


def multi(x, y):
    print(x)
    print(y)
    print(f"{x*y}\n")


def sub(x, y):
    print(x)
    print(y)
    print(f"{x-y}\n")


main()
