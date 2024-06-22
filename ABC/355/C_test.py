def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # グリッドを初期化
    grid = [[False]*n for _ in range(n)]

    # 数値からグリッド内の位置へのマップ
    pos = {(i-1)*n + j: (i-1, j-1) for i in range(1, n+1) for j in range(1, n+1)}

    # 各行、各列、各対角線のマークされていないマスの数
    rows = [n]*n
    cols = [n]*n
    diag = [n, n]

    for turn in range(t):
        # 宣言された数値をマーク
        x, y = pos[a[turn]]
        grid[x][y] = True

        # マークされていないマスの数を更新
        rows[x] -= 1
        cols[y] -= 1
        if x == y:
            diag[0] -= 1
        if x == n-y-1:
            diag[1] -= 1

        # ビンゴを確認
        if rows[x] == 0 or cols[y] == 0 or diag[0] == 0 or diag[1] == 0:
            print(turn + 1)
            return

    print(-1)


if __name__ == "__main__":
    main()