# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        
        def recursive_trees(i, j):
            if i > j:
                return [None]
            
            tmp = []
            for m in range(i, j+1):
                left = recursive_trees(i, m-1)
                right = recursive_trees(m+1, j)
                
                for l in left:
                    for r in right:
                        tmp.append(TreeNode(m, l, r))
            return tmp

        return recursive_trees(1, n)
