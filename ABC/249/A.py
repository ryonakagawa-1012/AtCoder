from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(types=str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    a, b, c, d, e, f, x = sep_read(int)

    takahashi = 0
    aoki = 0

    time = 0

    while time < x:
        time += 1

        # 高橋処理
        for i in range(c+1):
            if takahashi % a*b != i:
                takahashi += b


if __name__ == "__main__":
    main()
