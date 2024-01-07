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
    v, a, b, c = sep_read(int)

    while True:
        v -= a
        if v < 0:
            print("F")
            break

        v -= b
        if v < 0:
            print("M")
            break

        v -= c
        if v < 0:
            print("T")
            break


if __name__ == "__main__":
    main()
