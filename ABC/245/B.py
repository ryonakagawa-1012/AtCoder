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
    a = set(sep_read(int))
    num_set = set(list(range(2001)))

    print(min(num_set-a))


if __name__ == "__main__":
    main()
