def main():
    from builtins import print, list, int, sorted, map
    from sys import stdin
    from itertools import accumulate

    readline = stdin.readline

    n, k = map(int, readline().split())
    a = sorted(list(map(int, readline().split())))

    accm = list(accumulate(a, initial=0))

    print(accm)

    r = [0]*n

    for i in range(n):
        if i == 0:
            r[i] = 0
        else:
            r[i] = r[i-1]

        while r[i] < n-1 and accm[r[i]+2] - a[i] <= k:
            r[i] += 1

    print(r)
    ans = 0

    for i in range(n-1):
        ans += r[i]-i

    print(ans)


if __name__ == "__main__":
    main()
