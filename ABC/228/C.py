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
    n, k = sep_read(int)
    p = dict()
    for i in range(1, n+1):
        p[i] = sum(sep_read(int))

    sorted_p = sorted(p.items(), key=lambda pt: pt[1], reverse=True)
    # print(p)
    # print(sorted_p)

    ans = [""]*n

    lowest = sorted_p[k-1]
    for P in sorted_p:
        if P[1] + 300 >= lowest[1]:
            ans[P[0]-1] = "Yes"
        else:
            ans[P[0]-1] = "No"

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
