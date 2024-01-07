from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")


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


def bit_full_search(lst, n):
    ans = []

    for i in range(2**n):
        s_u_m = 0
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += lst[j]
        ans.append(s_u_m)

    return ans


def main():
    from collections import defaultdict
    n, w = sep_read(int)
    ab = defaultdict(int)
    for _ in range(n):
        at, bt = sep_read(int)
        ab[at] += bt

    ab = sorted(ab.items(), reverse=True)
    # print(ab)

    delicious = 0
    g = 0

    for i in range(len(ab)):
        delicious_t, g_t = ab[i]
        # print(delicious_t, g_t)
        if g < w:
            if g + g_t < w:
                delicious += delicious_t*g_t
                g += g_t
            else:
                delicious += delicious_t*(w-g)
                g = w
        else:
            print(delicious)
            exit()
        # print(delicious, g)

    print(delicious)


if __name__ == "__main__":
    main()
