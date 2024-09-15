def main():
    n = int(input())
    mg = int(input())

    g_matrix = list([False] * n for i in range(n))
    for _ in range(mg):
        v1, v2 = map(int, input().split())
        g_matrix[v1 - 1][v2 - 1] = True
        g_matrix[v2 - 1][v1 - 1] = True

    mh = int(input())

    h_matrix = list([False] * n for i in range(n))
    for _ in range(mh):
        at, bt = map(int, input().split())
        h_matrix[at - 1][bt - 1] = True
        h_matrix[bt - 1][at - 1] = True

    a = []
    for i in range(n - 1):
        at = [0] * (i + 1) + list(map(int, input().split()))
        a.append(at)

    # 上記でaはn-1まで埋まっているが、n-1行目だけ追加
    a.append([0] * n)

    ans = 0

    # グラフ G と H の比較を行い、異なる部分のコストを計算
    for i in range(n):
        for j in range(i + 1, n):
            if g_matrix[i][j] != h_matrix[i][j]:
                ans += a[i][j]

    print(ans)


if __name__ == "__main__":
    main()
