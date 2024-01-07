def main():
    from builtins import print, int, range
    from sys import stdin

    readline = stdin.readline

    b = int(readline())

    for a in range(1, 20):
        if a**a == b:
            print(a)
            exit()

    print(-1)

if __name__ == "__main__":
    main()
