N = int(input())
S = input()

T_Count = 0
A_Count = 0

if len([_ for _ in S if _ == "T"]) == len([_ for _ in S if _ == "A"]):  # 同点なら
    for i in range(N):
        if S[i] == "T":
            T_Count += 1
        elif S[i] == "A":
            A_Count += 1

        if T_Count == len([_ for _ in S if _ == "T"]):
            print("T")
            break
        if A_Count == len([_ for _ in S if _ == "A"]):
            print("A")
            break
elif len([_ for _ in S if _ == "T"]) > len([_ for _ in S if _ == "A"]):   # 高橋くんが勝ちなら
    print("T")
else:
    print("A")
