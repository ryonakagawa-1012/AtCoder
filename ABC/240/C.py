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
    n, x = sep_read(int)
    a, b = [0], [0]
    for _ in range(n):
        at, bt = sep_read(int)
        a.append(at)
        b.append(bt)

    dp = [[False]*(x+1) for _ in range(n+1)]

    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(x+1):
            if (0 <= j-a[i] and dp[i-1][j-a[i]]) or (0 <= j-b[i] and dp[i-1][j-b[i]]):
                dp[i][j] = True

    y_or_n(dp[n][x])


if __name__ == "__main__":
    main()
