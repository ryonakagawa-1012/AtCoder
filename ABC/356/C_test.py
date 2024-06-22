def main():
    n, m, k = map(int, input().split())
    tests = [list(map(int, input().split())) for _ in range(m)]
    results = [input() for _ in range(m)]

    count = 0
    for i in range(1 << n):
        keys = [False] * n
        for j in range(n):
            if (i >> j) & 1:
                keys[j] = True

        valid = True
        for test, result in zip(tests, results):
            c = sum(keys[j-1] for j in test)
            if (c >= k and result == 'x') or (c < k and result == 'o'):
                valid = False
                break

        if valid:
            count += 1

    print(count)


if __name__ == "__main__":
    main()