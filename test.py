MOD = 998244353


def count_strings(K, C):
    # dp[length][i][j] : length が i で、j 番目の文字が l 個含まれる場合の個数
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    dp[0][0] = 1  # 長さ0で、すべての文字が0個の文字列は1個（空文字列）

    for char_index in range(26):
        max_count = C[char_index]
        new_dp = [[0] * (K + 1) for _ in range(K + 1)]

        for length in range(K + 1):
            for count in range(K + 1):
                if dp[length][count] == 0:
                    continue

                for added in range(min(max_count, K - count) + 1):
                    new_length = length + added
                    new_count = count + added
                    if new_length <= K:
                        new_dp[new_length][new_count] += dp[length][count]
                        new_dp[new_length][new_count] %= MOD

        dp = new_dp

    # 長さ1以上K以下の文字列の個数を数える
    result = 0
    for length in range(1, K + 1):
        for count in range(K + 1):
            result += dp[length][count]
            result %= MOD

    return result


K = int(input())
C = list(map(int, input().split()))

# 結果の出力
print(count_strings(K, C))
