def main():
    from builtins import print, abs, int, range
    from sys import stdin

    readline = stdin.readline

    d = int(readline())

    r = int(d**0.5)
    ans = r

    for x in range(r+1):
        y1 = int(abs((d-x**2)**0.5))
        y2 = y1+1
        ans = min(ans, abs(x**2+y1**2-d), abs(x**2+y2**2-d))

    print(ans)

if __name__ == "__main__":
    main()
