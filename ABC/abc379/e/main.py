import sys
import time

def input():return sys.stdin.readline().rstrip()


def main():
    sys.set_int_max_str_digits(0)
    n = int(input())
    s = input()
    ans = 0
    f = 0
    for i in range(n):
        num = int(s[i])
        f = f*10 + num* (i + 1)
        ans += f
    print(ans)

if __name__ == '__main__':
    main()
