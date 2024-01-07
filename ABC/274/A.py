def main():
    from builtins import print, int, map, round, range, len
    from sys import stdin

    readline = stdin.readline
    
    a, b = map(int, readline().split())

    ans = list(str(round(b/a, 3)))

    for i in range(5-len(ans)):
        ans.append("0")

    print("".join(ans))

if __name__ == "__main__":
    main()
