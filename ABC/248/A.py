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
    s = set(list(input()))
    l1st = set(str(_) for _ in range(10))

    print("".join(l1st - s))


if __name__ == "__main__":
    main()
