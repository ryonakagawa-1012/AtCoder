def main():
    from builtins import print, list, int
    from sys import stdin

    readline = stdin.readline

    h, w = map(int, readline().split())
    c = list(readline().rstrip() for _ in range(h))

    ans =[]

    for i in range(w):
        ans.append(list(C[i] for C in c).count("#"))

    print(" ".join(str(_) for _ in ans))


if __name__ == "__main__":
    main()
