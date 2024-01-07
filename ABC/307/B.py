N = int(input())
S = [input() for i in range(N)]

Palindrome_Flag = False

for i in range(N):
    for j in range(N):
        string = S[i]
        if i != j:
            string += S[j]
            if string == string[::-1]:
                Palindrome_Flag = True

if Palindrome_Flag:
    print("Yes")
else:
    print("No")
