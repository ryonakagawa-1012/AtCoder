
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
    a = list(sep_read(int))
    b = list(sep_read(int))

    dp = [0]*(n+1)

    dp[1] = 0
    dp[2] = a[0]

    for i in range(3, n+1):
        dp[i] = min(dp[i-1]+a[i-2], dp[i-2] + b[i-3])

    print(dp[n])


if __name__ == "__main__":
    main()
