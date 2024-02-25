def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_kth_number(N, M, K):
    lcm_value = lcm(N, M)
    current_number = lcm_value
    count = 0

    while count < K:
        if current_number % N == 0 and current_number % M != 0:
            count += 1

        if current_number % M == 0 and current_number % N != 0:
            count += 1

        current_number += lcm_value

    return current_number - lcm_value

# 例として N=3, M=4, K=5 を使用
N = 3
M = 4
K = 5
result = find_kth_number(N, M, K)
print(result)
