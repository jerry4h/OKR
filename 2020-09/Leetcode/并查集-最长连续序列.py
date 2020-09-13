# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums_grp = [1 for _ in range(n)]
        rank = [1 for _ in range(n)]
        father = [i for i in range(n)]
        num2idx = dict()

        def find(u):
            if father[u] == u:
                return u
            else:
                return find(father[u])
        def union(u, v):
            fu, fv = find(u), find(v)
            ru, rv = rank[fu], rank[fv]
            if fu==fv:
                return True
            else:
                if ru < rv:
                    father[fu] = fv
                    nums_grp[fv] += nums_grp[fu]
                else:
                    father[fv] = fu
                    nums_grp[fu] += nums_grp[fv]
                    if ru==rv:
                        rank[fu] += 1
                return False

        for i, num in enumerate(nums):
            if num in num2idx:
                continue
            num2idx[num] = i
            for num_new in (num-1, num+1):
                if num_new not in num2idx:
                    continue
                union(i, num2idx[num_new])
        
        return max(nums_grp)
