def main():
    from sys import stdin
    from collections import defaultdict

    readline = stdin.readline

    n = int(readline())
    s = defaultdict(int)
    for _ in range(n):
        read = readline().rstrip()
        if s[read] == 0:
            print(read)
        else:
            print(read+"("+str(s[read])+")")
        s[read] += 1


if __name__ == "__main__":
    main()
