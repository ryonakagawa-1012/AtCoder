N = int(input())

j = [_ for _ in range(1, 10) if N % _ == 0]

s = []

for i in range(N+1):
    for j_ in range(len(j)):
        if i % (N/j[j_]) == 0:
            s.append(j[j_])
            break
        elif j_ == len(j) - 1:
            s.append("-")

print("".join(map(str, s)))
