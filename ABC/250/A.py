from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(types=str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    h, w = sep_read(int)
    r, c = sep_read(int)

    ans = 4

    if r - 0 == 1:
        ans -= 1
    if c - 0 == 1:
        ans -= 1
    if r - h == 0:
        ans -= 1
    if c - w == 0:
        ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
