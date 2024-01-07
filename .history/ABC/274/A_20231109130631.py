def main():
    from builtins import print, int, map
    from sys import stdin

    readline = stdin.readline
    
    a, b = map(int, readline().split())
    
    print(round(b/a, 5))


if __name__ == "__main__":
    main()
