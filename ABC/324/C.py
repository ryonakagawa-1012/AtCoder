N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

T_size = len(T)
ans = []
f_count = 0
b_count = 0

print(S[0][:1])

for i in range(N):
    if S[i] == T:
        ans.append(i+1)

    elif T_size-1 < len(S[i]) < T_size+1:
        f_flag = True
        b_flag = True
        for j in range(1, len(S[i])):

            if S[i][:j] == T[:j] and f_flag:
                f_count += 1
            else:
                f_flag = False

            if S[i][-1-j:-1] == T[-1-j:-1] and b_flag:
                b_count += 1
            else:
                b_flag = False

            if not (f_flag or b_flag):
                break
