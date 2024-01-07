N = int(input())

S = input()

A = 0
B = 0
C = 0

for i in range(N):
    if S[i] == "A":
        A = 1
    elif S[i] == "B":
        B = 1
    elif S[i] == "C":
        C = 1

    if A == B == C == 1:
        print(i+1)
        break
