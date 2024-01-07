def main():
    from builtins import print, list, range, exit
    from sys import stdin

    readline = stdin.readline

    s = list(readline().rstrip())
    t = list(readline().rstrip())

    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            exit()

    print(len(s)+1)


if __name__ == "__main__":
    main()
