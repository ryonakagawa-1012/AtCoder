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
    from bisect import bisect_left

    n, k = sep_read(int)
    a = list(sep_read(int))
    b = list(sep_read(int))
    c = list(sep_read(int))
    d = list(sep_read(int))

    ab = set()
    cd = set()

    for i in range(n):
        for j in range(n):
            ab.add(a[i]+b[j])
            cd.add(c[i]+d[j])

    cd = sorted(cd)

    # print(ab, cd)

    len_cd = len(cd)

    for AB in ab:
        index = bisect_left(cd, k-AB)
        if index < len_cd and cd[index] == k - AB:
            yes()
            exit()

    no()


if __name__ == "__main__":
    main()
