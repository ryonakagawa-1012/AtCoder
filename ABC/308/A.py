S = list(map(int, input().split()))

count_A = 0
count_C = 0

Condition_A = False
Condition_B = False
Condition_C = False

for i in range(7):
    if S[i] <= S[i+1]:
        count_A += 1
    if count_A == 7:
        Condition_A = True

if 100 <= S[0] and S[7] <= 675:
    Condition_B = True

for i in range(8):
    if S[i] % 25 == 0:
        count_C += 1
    if count_C == 8:
        Condition_C = True

# print(Condition_A)
# print(Condition_B)
# print(Condition_C)

if Condition_A and Condition_B and Condition_C:
    print("Yes")
else:
    print("No")
