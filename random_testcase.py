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

N = randint(1, 2*10**4)
S = "1"*N

print(N)
print(S)
