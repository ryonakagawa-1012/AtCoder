import sys
import decimal
from collections import defaultdict
from itertools import groupby
from functools import cache

from numpy.matrixlib.defmatrix import matrix


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


# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: "list[tuple]") -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res


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


finished = False


def dfs(pos, graph_lst, visited, path, goal):
    global finished
    if finished:
        return

    path.append(pos)
    visited[pos] = True
    if pos == goal:
        finished = True
        return

    for i in graph_lst[pos]:
        if not visited[i]:
            dfs(i, graph_lst, visited, path, goal)
            if finished:
                return

    path.pop()


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members


class Quadtree:
    def __init__(self, x_min, x_max, y_min, y_max, max_depth=5):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.max_depth = max_depth
        self.children = None
        self.is_filled = False

    def subdivide(self):
        mid_x = (self.x_min + self.x_max) / 2
        mid_y = (self.y_min + self.y_max) / 2
        self.children = [
            Quadtree(self.x_min, mid_x, self.y_min, mid_y, self.max_depth - 1),  # 左下
            Quadtree(mid_x, self.x_max, self.y_min, mid_y, self.max_depth - 1),  # 右下
            Quadtree(self.x_min, mid_x, mid_y, self.y_max, self.max_depth - 1),  # 左上
            Quadtree(mid_x, self.x_max, mid_y, self.y_max, self.max_depth - 1)   # 右上
        ]

    def insert(self, x_min, x_max, y_min, y_max):
        if self.max_depth == 0:
            self.is_filled = True
            return

        if not self.overlaps(x_min, x_max, y_min, y_max):
            return  # この領域と重ならない場合は何もしない

        if not self.children:
            self.subdivide()

        if self.contains_area(x_min, x_max, y_min, y_max):
            self.is_filled = True
            self.children = None  # 子ノードは不要
            return

        for child in self.children:
            child.insert(x_min, x_max, y_min, y_max)

        # 子ノードが全て塗りつぶされた場合、このノードも塗りつぶされたとみなす
        if all(child.is_filled for child in self.children):
            self.is_filled = True
            self.children = None

    def overlaps(self, x_min, x_max, y_min, y_max):
        return not (x_max <= self.x_min or x_min >= self.x_max or y_max <= self.y_min or y_min >= self.y_max)

    def contains_area(self, x_min, x_max, y_min, y_max):
        return self.x_min <= x_min and self.x_max >= x_max and self.y_min <= y_min and self.y_max >= y_max

    def calculate_filled_area(self):
        if self.is_filled:
            # このノードが塗りつぶされている場合、その面積を返す
            return (self.x_max - self.x_min) * (self.y_max - self.y_min)

        if not self.children:
            # このノードが塗りつぶされておらず、子ノードもない場合、面積は0
            return 0

        # 子ノードがある場合、各子ノードの面積を再帰的に計算
        total_area = 0
        for child in self.children:
            total_area += child.calculate_filled_area()
        return total_area

    def query(self, x, y):
        if self.is_filled:
            return True

        if not self.children:
            return False

        for child in self.children:
            if child.contains(x, y):
                return child.query(x, y)
        return False

    def contains(self, x, y):
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

    def remove(self, x_min, x_max, y_min, y_max):
        if not self.overlaps(x_min, x_max, y_min, y_max):
            return

        if self.max_depth == 0:
            self.is_filled = False
            return

        if not self.children:
            return

        for child in self.children:
            child.remove(x_min, x_max, y_min, y_max)

        if all(not child.is_filled and not child.children for child in self.children):
            self.children = None



# sys.setrecursionlimit(10 ** 6)


def input():return sys.stdin.readline().rstrip()


direction = {"U": (0, -1), "D":(0, 1), "L":(-1, 0), "R":(1, 0), "UL":(-1, -1), "UR":(1, -1), "DL":(-1, 1), "DR":(1, 1)}


def is_end(x: int, y: int, max_x: int, max_y: int, muki: str) -> bool:
    return {"U": y == 0, "D": y == max_y, "L": x == 0, "R": x == max_x}[muki]


def main():
    n = int(input())
    oxya = list(input().split())
    matrix = Quadtree(0, 10**6, 0, 10**6)
    for _ in range(n-1):
        oxya = list(input().split())
        o, x, y, a = oxya[0], int(oxya[1]), int(oxya[2]), int(oxya[3])
        if o == "+":
            matrix.insert(x, x+a-1, y+a-1, y)
        else:
            matrix.remove(x, x+a-1, y+a-1, y)

    print(matrix.contains(2, 2))
    print(matrix.calculate_filled_area())


if __name__ == "__main__":
    main()
