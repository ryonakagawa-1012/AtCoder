def main():
    from itertools import accumulate
    from bisect import bisect
    n, q = map(int, input().split())
    r = sorted(list(map(int, input().split())))
    accm = list(accumulate(r))
    for _ in range(q):
        x = int(input())
        print(bisect(accm, x))

if __name__ == '__main__':
    main()
