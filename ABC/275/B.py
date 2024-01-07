def main():
    from builtins import print, int, map
    from sys import stdin

    readline = stdin.readline

    a, b, c, d, e, f = map(int, readline().split())

    print(((a*b*c)-(d*e*f))%998244353)


if __name__ == "__main__":
    main()
