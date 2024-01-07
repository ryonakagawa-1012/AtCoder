def main():
    numbers = list(map(int, input().split()))
    numbers.sort()

    total = 0
    for i in range(len(numbers) - 1):
        total += abs(numbers[i] - numbers[i + 1])

    # 最小となる組み合わせの差の絶対値の合計を求める
    min_total = total
    for i in range(1, len(numbers) - 1):
        # 数列内の隣り合う要素をスキップして差の絶対値の合計を計算する
        diff = abs(numbers[i - 1] - numbers[i + 1]) - abs(numbers[i - 1] - numbers[i]) - abs(numbers[i] - numbers[i + 1])
        min_total = min(min_total, total - diff)

    print(min_total)


if __name__ == "__main__":
    main()
