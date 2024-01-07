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
    n, s = sep_read(int)
    a = [0] + list(sep_read(int))

    dp = [[False]*(s+1) for _ in range(n+1)]

    dp[0][0] = True

    for i in range(n+1):
        for j in range(s+1):
            if dp[i-1][j] or (0 <= j-a[i] and dp[i-1][j-a[i]]):
                dp[i][j] = True

    if dp[n][s]:
        ans = []
        place = s

        for i in range(1, n+1)[::-1]:
            if dp[i-1][place]:
                pass
            else:
                place -= a[i]
                ans.append(i)

        print(len(ans))
        print(*ans[::-1], sep=" ")
    else:
        print(-1)


if __name__ == "__main__":
    main()
