def main():
    from builtins import print, list, map, int, max
    from sys import stdin

    readline = stdin.readline

    n = readline()
    h = list(map(int, readline().split()))

    print(h.index(max(h))+1)


if __name__ == "__main__":
    main()
