def main():
    from builtins import int, map, list, print, sorted
    from sys import stdin

    readline = stdin.readline

    n, m = map(int, readline().split())
    a = sorted(list(map(int, readline().split())))

    ans = []

    for i in range(n):
        count = 0
        left, right = i, n
        while left < right:
            mid = (left + right) // 2
            if a[mid] < a[i] + m:
                count = mid - i + 1
                left = mid + 1
            else:
                right = mid

        ans.append(count)

    print(max(ans))

if __name__ == "__main__":
    main()
