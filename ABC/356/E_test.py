def calculate_floor_division_sum(n, a):
    a.sort()
    total = 0
    j = n
    for i in range(n-1, -1, -1):
        while j > 0 and a[j-1] > a[i] * 2:
            j -= 1
        total += n - j
        if i + 1 < n and a[i] == a[i + 1]:
            total -= 1
    return total // 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(calculate_floor_division_sum(n, a))

if __name__ == "__main__":
    main()