from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


def readline(back_slash=False):
    if back_slash:
        return stdin.readline()
    else:
        return stdin.readline().rstrip()


def sep_read(types=str):
    if types == str:
        return stdin.readline().rstrip().split()
    else:
        return map(types, stdin.readline().split())


def main():
    n = int(input())
    x, y = [], []
    for _ in range(n):
        xi, yi = sep_read(int)
        x.append(xi)
        y.append(yi)
    s = readline()
    


if __name__ == "__main__":
    main()
