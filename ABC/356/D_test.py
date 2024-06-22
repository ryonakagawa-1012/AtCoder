def popcount(x):
    return bin(x).count('1')

def bitDP(pos, tight, count, N, M, dp):
    if pos == -1:
        return count

    if dp[pos][tight][count] != -1:
        return dp[pos][tight][count]

    limit = (N >> pos) & 1 if tight else 1

    res = 0
    for digit in range(0, limit + 1):
        res += bitDP(
            pos - 1,
            tight and (digit == limit),
            count + popcount(digit & ((M >> pos) & 1)),
            N, M, dp
        )

    dp[pos][tight][count] = res
    return res

def solve(N, M):
    dp = [[[-1 for _ in range(65)] for _ in range(2)] for _ in range(65)]
    return bitDP(len(bin(N)) - 3, 1, 0, N, M, dp)


N, M = map(int, input().split())

# 結果を計算して出力
print(solve(N, M)%998244353)

