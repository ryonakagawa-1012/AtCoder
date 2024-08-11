def solve():
    N = int(input())
    S = [input() for _ in range(N)]

    # Mは最も長い文字列の長さ
    M = max(len(s) for s in S)

    # Tを初期化
    T = ['' for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if i < len(S[j]):
                T[i] += S[j][i]
            else:
                T[i] += '*'

    # Tの各要素の末尾が'*'であれば削除する
    for i in range(M):
        T[i] = T[i].rstrip('*')

    # 結果を出力
    for t in T:
        print(t)


# 入力例のテスト
solve()
