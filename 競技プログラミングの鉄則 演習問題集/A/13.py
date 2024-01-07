def main():
    from builtins import print, map, int, list, range
    from sys import stdin

    readline = stdin.readline

    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))

    r = [0]*n

    for i in range(n-1):
        if i == 0:
            r[i] = 0
        else:
            r[i] = r[i-1]

        while r[i] < n-1 and a[r[i]+1]-a[i] <= k:
            r[i] += 1

    print(r)
    ans = 0

    for i in range(n-1):
        ans += r[i]-i

    print(ans)

if __name__ == "__main__":
    main()
