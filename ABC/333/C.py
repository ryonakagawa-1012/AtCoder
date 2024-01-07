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
    n = int(readline())

    repunit = [int('1' * i) for i in range(1, 13)]

    # print(repunit)

    ans = set()

    for i in range(12):
        for j in range(i, 12):
            for k in range(j, 12):
                ans.add(repunit[i]+repunit[j]+ repunit[k])

    print(sorted(ans)[n-1])


if __name__ == "__main__":
    main()
