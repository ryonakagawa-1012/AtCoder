from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(types = str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    h, w = sep_read(int)
    a = list(sep_read(int) for _ in range(h))
    b = list(sep_read(int) for _ in range(h))




if __name__ == "__main__":
    main()
