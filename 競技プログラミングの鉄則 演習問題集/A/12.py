def check(m, a, n, k):
    sum = 0
    for i in range(n):
        sum += m // a[i]
    # print(m, k, sum)
    if k <= sum:
        return True
    else:
        return False
    

def main():
    from builtins import int, map, list
    from sys import stdin

    readline = stdin.readline

    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    # A.insert(0, 0)

    left = 0
    right = 10**9

    while left < right:
        # print(left, right)
        mid = (left+right)//2

        # print(check(mid, A, N, K))
        if check(mid, A, N, K):
            right = mid
        else:
            left = mid+1

    print(left)

if __name__ == "__main__":
    main()
