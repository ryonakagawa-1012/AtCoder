S = input()

S_len = len(S)

Count_odd = [1]*(S_len-2)
Count_even = [2]*(S_len-2)

even_flag = 0

# print(Count_odd)
# print(Count_even)


for i in range(1, S_len-1):
    for j in range(1, S_len):
        if 0 <= i-j and i+j <= S_len-1:  # 配列外参照防止
            if S[i-j] == S[i+j]:
                Count_odd[i-1] += 2
        if S[i] == S[i+1]:  # 偶数だったら
            even_flag = 1
            if 0 <= i-j and i+j+1 <= S_len-1:  # 配列外参照防止
                if S[i-j] == S[i+j+1]:
                    Count_even[i-1] += 2
                    even_flag = 1

# print(Count_odd)
# print(Count_even)

if even_flag == 1:
    print(max(max(Count_odd), max(Count_even)))
else:
    print(max(Count_odd))
