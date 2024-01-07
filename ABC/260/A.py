from collections import Counter


def inverse_dic(dictionary):
    return {v: k for k, v in dictionary.items()}


s = Counter(input())
print(inverse_dic(s).get(1, -1))
