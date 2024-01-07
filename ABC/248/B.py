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
    a, b, k = sep_read(int)
    ans = 0

    while a < b:
        ans += 1
        a *= k

    print(ans)


if __name__ == "__main__":
    main()
