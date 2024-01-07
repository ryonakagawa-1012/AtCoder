def main():
    from builtins import print, map, int, list, range
    from sys import stdin

    readline = stdin.readline

    n, q = map(int, readline().split())
    s = readline().strip()
    lr = list(list(map(int, readline().split())) for _ in range(q))

    accmu = [0] * n

    for i in range(1, n):
        accmu[i] = accmu[i - 1] + (s[i - 1] == s[i])

    # print(accmu)

    for i in range(q):
        l, r = lr[i]
        ans = accmu[r - 1] - accmu[l - 1]
        print(ans)

if __name__ == "__main__":
    main()
