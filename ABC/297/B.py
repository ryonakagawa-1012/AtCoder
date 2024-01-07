def check_odd_even_diff(num1, num2):
    if (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0):
        return True
    else:
        return False


def k_between_r(s):
    r_flag = False
    k_flag = False
    for char in s:
        if char == "R":
            r_flag = True
            if k_flag:
                return True
        if char == "K" and r_flag:
            k_flag = True

    return False


S = input()

Flag_1 = False
Flag_2 = False

B_num = []

for i in range(8):
    if S[i] == "B":
        B_num.append(i)

Flag_1 = check_odd_even_diff(B_num[0], B_num[1])
Flag_2 = k_between_r(S)

# print(Flag_1)
# print(Flag_2)

if Flag_1 and Flag_2:
    print("Yes")
else:
    print("No")
