from sys import stdin
from itertools import combinations

def sep_read(types=str):
    if types == str:
        return stdin.readline().rstrip().split()
    else:
        return map(types, stdin.readline().split())


def is_valid(arr):
    for i in range(len(arr) // 2):
        if arr[2 * i + 1] >= arr[2 * i + 2]:
            return False
    return True


def generate_valid_combinations(arr, len_arr):
    for p in combinations(arr, len_arr):
        if is_valid(p):
            yield p


def main():
    from collections import defaultdict

    n, q = sep_read(int)
    z = list(sep_read(int))

    a = list(range(2*n+1))

    # perms = permutations(a)

    fa_list = defaultdict(int)

    for p in generate_valid_combinations(a, 2*n+1):
        print(p)
        b = [p[0]]
        for i in range(n):
            b.append(min(max(b[i], p[2*i+1]), p[2*i+2]))
        # print(b)
        fa_list[b[-1]] += 1

    # print(fa_list)

    ans = []

    for Z in z:
        ans.append(fa_list[Z] % 998244353)

    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
