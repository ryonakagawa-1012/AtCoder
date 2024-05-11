import sys
import decimal


def yes():
    print("Yes")


def no():
    print("No")


def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")


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


def atcoder():
    """
    リスト ['a', 't', 'c', 'o', 'd', 'e', 'r'] を作成する関数

    Returns
    -------
    return : list
        ['a', 't', 'c', 'o', 'd', 'e', 'r']
    """
    return list("atcoder")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


def readline(back_slash=False):
    """
    文字を受け取る関数(input()を短く、高速化した関数)

    Parameters
    ----------
    back_slash : bool
        末尾の\\nまで読み取るかどうか(デフォルトはFalse)

    Returns
    -------
    return : str
        受け取った文字
    """
    if back_slash:
        return sys.stdin.readline()
    else:
        return sys.stdin.readline().rstrip()


def sep_read(types=str):
    """
    複数の文字を受け取る関数(input().sprit()を短く、高速化した関数)

    Parameters
    ----------
    types : type
        受け取った値をキャストする型(デフォルトはstr型)

    Returns
    -------
    return : list or map
        typesによって異なる
    """
    if types == str:
        return sys.stdin.readline().rstrip().split()
    else:
        return map(types, sys.stdin.readline().split())


def read_multi_line_input():
    """
    複数行の数字を受け取る関数

    Returns
    -------
    return : list
        受け取った数字のリスト
    """
    a = []
    while True:
        try:
            a.append(int(input()))
        except EOFError:
            break
    return a


def bit_full_search(lst, n):
    """
    ビット全探索する関数

    Parameters
    ----------
    lst : list
        ビット全探索したいリスト
    n : int
        リストの要素数

    Returns
    -------
    return : list
        ビット全探索した結果のリスト
    """
    ans = []
    for i in range(2 ** n):
        s_u_m = 0
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += lst[j]
        ans.append(s_u_m)

    return ans


def rounding(num, digit):
    """
    四捨五入を正確にする関数

    Parameters
    ----------
    num : float or int or str
        四捨五入したい数
    digit : int
        丸める桁数（小数点以下の場合は負の値を指定）

    Returns
    -------
    return : decimal.Decimal
        四捨五入された数値

    Notes
    -----
    - digitが2以上の場合(2桁目以降に丸める時)、指数表記になるのでキャストが必要
    """
    deci = 10 ** digit
    return (decimal.Decimal(str(num)).
            quantize(decimal.Decimal(str(deci) if deci < 1 else "1E" + str(digit - 1)), decimal.ROUND_HALF_UP))


def print_2d(lst, sep=None):
    """
    2次元配列を出力する関数

    Parameters
    ----------
    lst : list
        出力したい2次元配列
    sep : str
        区切り文字(デフォルトはNone)
    """
    for LIST in lst:
        print(*LIST, sep=sep)


class Deque:
    """
    O(1)でランダムアクセスできるdeque
    """

    def __init__(self, src_arr=[], max_len=300000):
        self.N = max(max_len, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l: raise IndexError('index out of range: ' + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1: self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full(): self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N

    def appendleft(self, x):
        if self.is_full(): self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N

    def pop(self):
        if self.is_empty(): raise IndexError('pop() when buffer is empty')
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret

    def popleft(self):
        if self.is_empty(): raise IndexError('popleft() when buffer is empty')
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret

    def rotate(self, n=1):
        if n > 0:
            for _ in range(n):
                self.appendleft(self.pop())
        else:
            for _ in range(abs(n)):
                self.append(self.popleft())

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return 'Deque({0})'.format(str(list(self)))


class unionfind:
    # n 頂点の Union-Find 木を作成
    # （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)  # 最初は親が無い
        self.size = [1] * (n + 1)  # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


def main():
    from collections import defaultdict
    n, m = sep_read(int)
    graph_lst = defaultdict(set)
    for i in range(m):
        at, bt = sep_read(int)
        graph_lst[at].add(bt)
        graph_lst[bt].add(at)

    follower = -float("inf")
    influencer = 0
    for i in range(1, m+1):
        if follower < len(graph_lst[i]):
            follower = len(graph_lst[i])
            influencer = i

    print(influencer)


if __name__ == "__main__":
    main()
