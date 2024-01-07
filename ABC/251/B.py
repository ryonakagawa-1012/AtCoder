from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(types = str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    n, w = sep_read(int)
    a = list(sep_read(int))

    ans = 0

    for i in range(n):
        if a[i] < w:
            ans += 1
        for j in range(i+1, n):
            if a[i] + a[j] < w:
                ans += 1
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] < w:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
