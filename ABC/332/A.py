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
    n, s, k = sep_read(int)
    pq_sum = 0

    for _ in range(n):
        p, q = sep_read(int)
        pq_sum += p * q

    if pq_sum < s:
        pq_sum += k

    print(pq_sum)


if __name__ == "__main__":
    main()
