N = list(input())

N_int = int("".join(N))

# print(N)
# print("".join(N))
#
# N[0] = "0"
#
# print(N)
# print("".join(N))

if N_int < 10**3:
    print("".join(N))

for i in range(6):
    if 10**(3+i) <= N_int < 10**(4+i):
        zeros = ["0"] * (i + 1)
        N[-(i + 1):] = zeros
        print("".join(N))
