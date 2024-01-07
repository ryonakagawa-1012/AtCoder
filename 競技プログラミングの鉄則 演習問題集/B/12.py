def check(mid, n):
    if mid**3 + mid > n:
        return True
    else:
        return False

def main():
    from builtins import int, print
    from sys import stdin

    readline = stdin.readline

    n = int(readline())

    left = 0.0
    right = 100.0

    for _ in [0]*20:
        mid = (left+right)/2

        if check(mid, n):
            right = mid
        else:
            left = mid

    print(mid)


if __name__ == '__main__':
    main()
