# 地图上有 m 条无向边，每条边 (x, y, w) 表示位置 m 到位置 y 的权值为 w。从位置 0 到 位置 n 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。请问从位置 0 到 位置 n 所有路径中最小的危险值为多少？

# 最小危险值为最小生成树中 0 到 n 路径上的最大边权。

# Kruskal's algorithm
class Solution:
    def getMinRiskValue(self, N, M, X, Y, W):
        
        # Kruskal's algorithm with union-find
        parent = list(range(N + 1))
        rank = [1] * (N + 1)
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            
            return True
        
        # 排序很关键
        edges = sorted(zip(W, X, Y))
        
        for w, x, y in edges:
            # 慢慢扩充图形，如果扩充导致了0和N相连，则肯定是新的边导致的
            if union(x, y) and find(0) == find(N): # early return without constructing MST
                return w