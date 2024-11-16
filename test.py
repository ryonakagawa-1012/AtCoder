class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n  

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]  
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]  
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size[self.find(x)]  
