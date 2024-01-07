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
    from collections import defaultdict
    q = int(input())

    s = defaultdict(int)
    max_s = 0
    min_s = float("inf")
    for _ in range(q):
        query = list(sep_read(int))
        if query[0] == 1:
            x = query[1]
            s[x] += 1
            max_s = max(max_s, x)
            min_s = min(min_s, x)
        elif query[0] == 2:
            x = query[1]
            c = query[2]
            s[x] -= min(c, s[x])
            if s[x] == 0:
                del s[x]
                if x == max_s:
                    max_s = max(s) if s else float('-inf')
                if x == min_s:
                    min_s = min(s) if s else float('inf')
        else:
            print(max_s-min_s)
        # print(dict(s))


if __name__ == "__main__":
    main()
