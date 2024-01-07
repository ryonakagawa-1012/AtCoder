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
    s = list(input())

    ans = s[:]

    ans[0] = "0"

    for i in range(3):
        ans[i+1] = s[i]

    print(*ans, sep="")


if __name__ == "__main__":
    main()
