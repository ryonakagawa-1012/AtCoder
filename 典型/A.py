def main():
    from bisect import bisect
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if a[-1] < k:
        print(-1)
    else:
        print(bisect(a, k))

if __name__ == '__main__':
    main()
