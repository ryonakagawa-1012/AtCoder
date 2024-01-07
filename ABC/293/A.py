S = list(input())

for i in range(len(S)//2):
    tmp = S[2*i]
    S[2*i] = S[2*i+1]
    S[2*i+1] = tmp

print("".join(S))
