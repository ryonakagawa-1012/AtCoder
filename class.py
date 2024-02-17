data = [1, 2, 1, 1, 4, 3, 9]
# data = list(map(int, input().split()))
purge = [] #purge : [動詞]〜を粛清する

# 粛清すべき要素のインデックスを探す
tmp = data[0] - 1
for i, e in enumerate(data):
    if e < tmp:
        purge.append(i)
    else:
        tmp = e

print(purge)

# Let's 粛清!!
for i, e in enumerate(purge):
    print(i, e)
    data.pop(e - i)
    print(data)

print(data)
