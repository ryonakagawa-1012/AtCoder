def main():
    from builtins import print, list, range, int, map, sorted
    from sys import stdin
    import numpy as np

    readline = stdin.readline

    a = np.array(list(list(map(int, readline().split())) for _ in range(9)))

    cond1 = True
    cond2 = True
    cond3 = True

    for i in range(9):
        if sorted([_ for _ in range(1, 10)]) != sorted(a[i]):
            cond1 = False
        if sorted([_ for _ in range(1, 10)]) != sorted(a[:, i:i+1].flatten()):
            cond2 = False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # print(a[i:i+3, j:j+3])
            if sorted([_ for _ in range(1, 10)]) != sorted(a[i:i+3, j:j+3].flatten()):
                cond3 = False

    # print(cond1)
    # print(cond2)
    # print(cond3)

    if cond1 and cond2 and cond3:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
