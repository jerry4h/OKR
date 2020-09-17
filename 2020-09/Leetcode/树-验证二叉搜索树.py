# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def getTreeInfo(root):
            """返回格式：该树的最小值、最大值、是否为BST，这种方法从底而上，需要遍历所有节点
            """
            if root is None:
                return None, None, True
            val = root.val
            vmin, vmax, status = val, val, True
            
            # 遍历左右
            lmin, lmax, lbst = getTreeInfo(root.left)
            rmin, rmax, rbst = getTreeInfo(root.right)
            if not lbst or not rbst:
                status = False
            if lmax is not None and lmax >= val:
                status = False
            if rmin is not None and rmin <= val:
                status = False
            # 该树的最大最小值与左右子树、本节点有关。
            vmin = lmin if lmin is not None else vmin
            vmax = rmax if rmax is not None else vmax
            return vmin, vmax, status

        if root is None:
            return True
        
        rst = getTreeInfo(root)
        return rst[-1]

    def isValidBST2(self, root:TreeNode) -> bool:
        """ 更容易的方法，自上而下，二分法。
        左边的数值范围应该在(-float("inf"), val)
        右边的在(val, float("inf"))
        """

    def isValidBST3(self, root:TreeNode) -> bool:
        """ 中序遍历比较大小
        """
