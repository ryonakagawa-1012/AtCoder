def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    S = data[1:N+1]

    M = max(len(s) for s in S)

    T = ['' for _ in range(M)]

    for i in range(N):
        s = S[i]
        for j in range(len(s)):
            T[j] = T[j] + s[j]
        for j in range(len(s), M):
            T[j] = T[j] + '*'

    for t in T:
        print(t)

if __name__ == "__main__":
    main()