N = int(input())
Water_Station = [i for i in range(101) if i % 5 == 0]
tmp = [0]*int(len(Water_Station))
for i in range(len(Water_Station)):
    tmp[i] = abs(Water_Station[i]-N)
print(Water_Station[tmp.index(min(tmp))])
