import sys


def input():return sys.stdin.readline().rstrip()


def main():
    h, w, k = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    


if __name__ == '__main__':
    main()
