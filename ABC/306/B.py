A = list(map(int, input().split()))

sum = 0

for i in range(64):
    sum += A[i]*2**i

print(sum)
