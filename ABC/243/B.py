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
    n = int(input())
    a = list(sep_read(int))
    b = list(sep_read(int))

    ans1 = 0
    ans2 = 0

    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        elif a[i] in b:
            ans2 += 1

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
