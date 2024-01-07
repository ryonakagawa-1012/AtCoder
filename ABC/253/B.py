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
    h, w = sep_read(int)
    s = list(input() for _ in range(h))
    # print(s)

    x, y = [], []

    for i in range(h):
        ss = s[i]
        for j in range(w):
            if ss[j] == "o":
                x.append(j)
                y.append(i)

    print(abs(x[0]-x[1])+abs(y[0]-y[1]))


if __name__ == "__main__":
    main()
