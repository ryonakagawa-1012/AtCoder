from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))

    max_value = max(a)
    count = Counter(a)

    accm = [0] * (max_value + 2)

    for i in range(1, max_value + 1):
        accm[i] = accm[i - 1] + count[i] * i

    ans = []

    for i in range(n):
        ans.append(accm[max_value] - accm[a[i]])

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
