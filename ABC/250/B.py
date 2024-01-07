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
    n, a, b = sep_read(int)
    


if __name__ == "__main__":
    main()
