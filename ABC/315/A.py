S = input()

result = ""

for i in range(len(S)):
    if S[i] != "a" and S[i] != 'e' and S[i] != 'i' and S[i] != 'o' and S[i] != 'u':
        result += S[i]


print(result)
