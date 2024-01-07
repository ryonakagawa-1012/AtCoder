N = int(input())
S = input()

in_Flag = False

for i in range(N):
    if S[i] == "|":
        for j in range(1, N-i):
            if S[i+j] == "*":
                for k in range(1, N-i-j):
                    if S[i+j+k] == "|":
                        in_Flag = True

if in_Flag:
    print("in")
else:
    print("out")
