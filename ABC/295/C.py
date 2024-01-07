def main():
    from builtins import print, map, int, list
    from sys import stdin
    import collections

    readline = stdin.readline

    n = int(readline())
    a = list(map(int, readline().split()))

    ans = 0
    counter = collections.Counter(a)
    # print(counter)

    for A in counter:
        ans += counter[A] // 2

    print(ans)


if __name__ == "__main__":
    main()
