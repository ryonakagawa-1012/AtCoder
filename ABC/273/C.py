def main():
    from sys import stdin

    readline = stdin.readline

    n = int(readline())
    a = list(map(int, readline().split()))

    a_kind = sorted(set(a))
    a_kind_len = len(a_kind)
    print(a_kind_len)
    print(a_kind)

    for A in a:
        print(a_kind.index(A), a_kind_len - (a_kind.index(A) + 1))


if __name__ == "__main__":
    main()
