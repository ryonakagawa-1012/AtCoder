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
import sys
sys.set_int_max_str_digits(0)

N = randint(10**5, 2*10**5)
S = "9"*N

print(N)
print(S)
