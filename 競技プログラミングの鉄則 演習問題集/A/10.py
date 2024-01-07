def main():
    from builtins import (int, map, list, max, print)
    from itertools import accumulate
    from sys import stdin

    readline = stdin.readline

    N = int(readline())
    A = list(map(int, readline().split()))
    D = int(readline())
    P = list(accumulate(A, func=max, initial=0))
    Q = list(accumulate(A[::-1], func=max, initial=0))
    for _ in [0]*D:
        L, R = map(int, readline().split())
        print(max(P[L - 1], Q[N - R]))

if __name__ == "__main__":
    main()
