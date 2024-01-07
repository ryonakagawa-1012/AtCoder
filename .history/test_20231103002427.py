# 実行内容をmain関数に入れることで実行速度を上げている
def main():
    # 使用する関数をインポートすることで実行速度を上げている
    from builtins import int, print, range, str
    from sys import stdin

    import numpy as np

    readline = stdin.readline

    # A, Bの配列の初期化
    A = [[], []]
    B = [[], []]

    # 配列Aの入力
    for a in A:
        for i in range(2):
            a.append(int(readline()))

    # 配列Bの入力
    for b in B:
        for i in range(2):
            b.append(int(readline()))

    # A, Bを行列にキャストした後、Cに計算結果を代入
    C = np.matrix(A) + np.matrix(B)

    # 出力
    for c in C.tolist():
        print(" ".join(str(cc) for cc in c))


if __name__ == "__main__":
    main()
