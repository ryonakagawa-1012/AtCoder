def main():
    L, R = map(int, input().split())
    ans = []
    while L < R:
        x = L
        while (x | (x + 1)) <= R:
            x |= x + 1
        ans.append((L, x + 1))
        L = x + 1
    if L == R:
        ans.append((L, R))
    print(len(ans))
    for l, r in ans:
        print(l, r)

if __name__ == "__main__":
    main()
