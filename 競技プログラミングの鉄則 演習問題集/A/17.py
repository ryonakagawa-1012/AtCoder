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
    n = int(readline())
    a = [0,0]+list(sep_read(int))
    b = [0,0,0]+list(sep_read(int))

    dp = [0]*(n+1)

    dp[1] = 0
    dp[2] = a[2]

    for i in range(3, n+1):
        dp[i] = min(a[i]+dp[i-1], b[i]+dp[i-2])

    # print(dp[n])

    ans = [n]
    place = n

    while place != 1:

        if dp[place-1] + a[place] == dp[place]:
            place -= 1
        else:
            place -= 2

        ans.append(place)

    print(len(ans))
    print(*ans[::-1], sep=" ")


if __name__ == "__main__":
    main()
