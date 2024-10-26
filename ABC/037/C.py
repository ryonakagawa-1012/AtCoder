def main():
    from itertools import accumulate
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    accm = [0] + list(accumulate(a))

    # print(accm)

    ans = 0
    for i in range(n-k+1):
        ans += accm[i+k] - accm[i]

    print(ans)

if __name__ == '__main__':
    main()
