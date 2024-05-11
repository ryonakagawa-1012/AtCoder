from decimal import *
hugou = {"A": 0.05, "B": 0.30, "C": 0.07, "D": 0.04, "E": 0.15, "F": 0.20, "G": 0.09, "H": 0.10}
hugou = (sorted(hugou.items(), key=lambda x: x[1])[::-1])
print(hugou)
max_len = sum(Decimal(str(hugou[i][1])) for i in range(4, len(hugou)))
print(max_len)
print(max_len/2)
