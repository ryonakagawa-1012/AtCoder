from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


def sep_read(types=str):
    if types == str:
        return stdin.readline().rstrip().split()
    else:
        return map(types, stdin.readline().split())


def main():
    a, b, c, x = sep_read(int)

    if x <= a:
        print(1)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0)


if __name__ == "__main__":
    main()
