def a_to_z(lower=True):
    """
    a~zまたはA~Zが入ったリストを作成する関数

    Parameters
    ----------
    lower : bool
        小文字か大文字か(デフォルトは小文字)

    Returns
    -------
    return : list
        a~zまたはA~Zが入ったリスト
    """
    return list(chr(ord("a" if lower else "A") + i) for i in range(26))


from random import randint
# N = randint(1, 10000)
# D = randint(1, 10000)
# A = [randint(1, 10000) for i in range(N)]
# print(N, D)
# print(*A)

abc = a_to_z()
test = [abc[randint(0, 25)] for i in range(10000)]
print(*test, sep="")