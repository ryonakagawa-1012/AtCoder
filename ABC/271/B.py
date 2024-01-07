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
    n, q = sep_read(int)
    a = list(list(sep_read(int)) for _ in range(n))
    for _ in range(q):
        s, t = sep_read(int)
        print(a[s-1][t])


if __name__ == "__main__":
    main()
