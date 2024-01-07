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
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    a, b, c, d = sep_read(int)

    if a == c:
        if b == d:
            takahashi()
        elif b < d:
            takahashi()
        else:
            aoki()
    elif a < c:
        takahashi()
    else:
        aoki()


if __name__ == "__main__":
    main()
