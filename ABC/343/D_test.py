from collections import defaultdict


def main():
    n, t = map(int, input().split())
    s = defaultdict(int)

    unique_values_count = 0  # 初期状態での異なる値の数

    for _ in range(t):
        at, bt = map(int, input().split())

        # at の値を更新する前の値の出現回数を減らす
        if s[at] == 1:
            unique_values_count -= 1

        # at の値を更新
        s[at] += bt

        # at の値を更新した後の値の出現回数を増やす
        if s[at] == 1:
            unique_values_count += 1

        # 現在の異なる値の数を出力
        print(unique_values_count)


if __name__ == "__main__":
    main()
