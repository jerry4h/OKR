# [78] 子集
#

# @lc code=start
class Solution:
    def subsetsWRONG(self, nums: List[int]) -> List[List[int]]:
        # 写法有重复，待查TODO
        result = []
        def backtrack(i, tmp):
            """表示从第i个开始考虑。
            此时的tmp
            """
            print(i, tmp)
            n = len(nums)
            if i == n-1:
                result.append(tmp[:])
                result.append(tmp[:]+[nums[-1]])
                return
            
            # 第i个没选
            backtrack(i+1, tmp)
            # 第i个选了
            tmp.append(nums[i])
            for j in range(i+1, n):
                backtrack(j, tmp)
            tmp.pop()

        backtrack(0, [])
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  
