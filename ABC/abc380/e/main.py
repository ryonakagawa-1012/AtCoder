from collections import defaultdict
import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()

from collections import defaultdict


class PersistentPartUnionFind:
    def __init__(self,N):
        INF = float('INF')
        self.now = 0
        self.N = 0
        self.parent = [-1 for i in range(N)]
        self.time = [INF for i in range(N)]
        self.num = [[] for i in range(N)]
        for i in range(N):
            self.num[i].append((0,1))
    
    def find(self,t,x):
        '''
        version:tにおけるxの根を見つける
        t (any) : version
        x (int) : 要素
        return : int : 根
        '''
        while self.time[x] <= t:
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        '''
        x,yをつなげる
        x (int) : 要素
        y (int) : 要素
        '''
        self.now += 1
        x = self.find(self.now,x)
        y = self.find(self.now,y)

        if x == y:
            return
        
        if self.parent[x] > self.parent[y]:
            x,y = y,x
        
        
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.time[y] = self.now
        self.num[x].append((self.now,-self.parent[x]))

    def same(self,t,x,y):
        '''
        version:tにおけるx,yが同じかどうかO(logN)
        t (any) : version
        x (int) : 要素
        y (int) : 要素
        return : bool : 同じかどうか
        '''
        return self.find(t,x) == self.find(t,y)

    def size(self,t,x):
        '''
        version:tにおける要素xが含まれる集合の大きさ
        t (any) : version
        x (int) : 要素
        return : int :集合の大きさ  
        '''
        x = self.find(t,x)

        ok = 0
        ng = len(self.num[x])
        while (ng-ok > 1):
            mid = (ok+ng)>>1
            if self.num[x][mid][0] <= t:
                ok = mid
            else:
                ng = mid
        
        return self.num[x][ok][1]



def main():
    n, q = map(int, input().split())
    masu = PersistentPartUnionFind(n+1)
    for _ in range(q):
        query = input()
        if query[0] == "1":
            x, c = int(query[2]), int(query[-1])
            masu.union(x, c)
        else:            
            c = int(query[-1])
            print(masu.size(q+1, c))


if __name__ == '__main__':
    main()
