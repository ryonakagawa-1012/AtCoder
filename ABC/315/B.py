M = int(input())

D = list(map(int, input().split()))

Sum_1 = int(sum(D, 1)/2)

# print(Sum_1)

Sum_2 = 0

a = 0
b = 0

for i in range(M):
    Sum_2 += D[i]
    # print(i)
    # print(Sum_2)
    if Sum_2 >= Sum_1:
        a = i+1
        break

for i in range(1, D[a-1]+1):
    b = Sum_2 - D[a-1] + i
    if b == Sum_1:
        b = i
        break

print(a, b)
