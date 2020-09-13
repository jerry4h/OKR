# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        if n == 0 or len(edges[0]) == 0:
            return None
        father = [i for i in range(n+1)]

        def get_root(i):
            if father[i] == i:
                return i
            else:
                return get_root(father[i])
        def union(i, j):
            fi = get_root(i)
            fj = get_root(j)
            if fi == fj:
                return True
            else:
                father[fi] = fj
                return False

        for u, v in edges:
            if union(u, v):
                return (u, v)


'''
Accepted
39/39 cases passed (72 ms)
Your runtime beats 63.93 % of python3 submissions
Your memory usage beats 11.41 % of python3 submissions (14.3 MB)
'''
