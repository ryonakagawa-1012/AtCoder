def main():
    from builtins import print
    from sys import stdin

    readline = stdin.readline

    n, l, r = map(int, readline().split())
    a = list(map(int, readline().split()))

    for A in a:
        if l < A < r:
            print(A)
        elif l-A>=0:
            print(l)
        else:
            print(r)


if __name__ == "__main__":
    main()
