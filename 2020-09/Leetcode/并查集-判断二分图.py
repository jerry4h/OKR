# [785] 判断二分图
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        if n == 0:
            return
        
        father = [i for i in range(n)]
        num_graph = n
        
        def get_father(i):
            if i == father[i]:
                return i
            else:
                return get_father(father[i])
        def is_union(i, j):
            fi = get_father(i)
            fj = get_father(j)
            if fi == fj:
                return True
            else:
                return False
        def union(i, j):
            fi = get_father(i)
            fj = get_father(j)
            if fi == fj:
                return False
            father[fi] = fj
            return True

        for u in range(n):
            dst = graph[u]
            for v in dst:
                if is_union(v, u):
                    return False
                if union(v, dst[0]):
                    num_graph -= 1

        return True 
        # return num_graph == 2 # 不符题意，不是一个图也算
