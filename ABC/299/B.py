N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

T_list = {}

if T in C:
    T_list = {i+1: R[i] for i in range(N) if C[i] == T}
else:
    T_list = {i+1: R[i] for i in range(N) if C[i] == C[0]}

# print(T_list)

print(max(T_list, key=T_list.get))
