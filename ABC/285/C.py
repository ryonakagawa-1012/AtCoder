def alpha_to_base26(string):
    alpha_to_num = {chr(ord("A")+i-1):i for i in range(1, 27)}
    num = 0
    for s in string:
        num *= 26
        num += alpha_to_num[s]
    return num

def main():
    from builtins import print
    from sys import stdin

    readline = stdin.readline

    print(alpha_to_base26(readline().rstrip()))

if __name__ == "__main__":
    main()
