# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            """
            返回：最大高度、是否为平衡
            """
            if not node:
                return 0, True
            hl, sl = helper(node.left)
            hr, sr = helper(node.right)
            hn = max(hl, hr) + 1
            sn = True
            if not sl or not sr or (hl-hr)**2 > 1:
                sn = False
            return hn, sn
        
        h, s = helper(root)
        return s
        