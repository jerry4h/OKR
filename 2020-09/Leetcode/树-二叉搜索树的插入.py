# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """找到一个位置，插入
        1 val比p.val小，但p.left is None
        2 val比p.val大，但p.right is None
        """
        valNode = TreeNode(val)
        if root is None:
            return valNode
        p = root
        while True:
            if val < p.val:
                if p.left is None:
                    p.left = valNode
                    return root
                p = p.left
            elif val > p.val:
                if p.right is None:
                    p.right = valNode
                    return root
                p = p.right
            else:
                # val == p.val 不存在
                return root
