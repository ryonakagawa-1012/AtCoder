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
    n = int(input())
    h = [0] + list(sep_read(int))

    dp = [0]*(n+1)

    dp[1] = 0
    dp[2] = abs(h[1]-h[2])

    for i in range(3, n+1):
        dp[i] = min(abs(h[i-1]-h[i])+dp[i-1], abs(h[i-2]-h[i])+dp[i-2])

    print(dp[n])


if __name__ == "__main__":
    main()
