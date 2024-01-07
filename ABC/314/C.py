def index_find(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def main():
    from builtins import print, map, int, list
    from sys import stdin

    readline = stdin.readline

    n, m = map(int, readline().split())
    s = readline().rstrip()
    c = list(map(int, readline().split()))

    ans = s

    for i in range(1, m):
        shift_list = index_find(s, i)



if __name__ == "__main__":
    main()
