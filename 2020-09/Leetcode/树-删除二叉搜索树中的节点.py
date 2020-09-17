# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 关键在于两点：
        # 1 二叉搜索树的中序遍历性质
        # 2 删除某个节点相当于替换问题
        # 3 链表中，去掉某个节点，必须从父节点操作。
        if root is None:
            return None
        dummy = TreeNode(float("inf"), left=root)

        # 找到对应节点
        pre, cur = dummy, dummy.left
        while cur is not None:
            if cur.val == key:
                break
            pre = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            return root
        
        # 判断节点的情况
        if cur.left is None and cur.right is None:
            # del cur
            if pre.right is cur:
                pre.right = None
            else:
                pre.left = None
        elif cur.left is not None:
            # 找到前驱节点：左子树中最大的节点
            precessor = cur.left
            while precessor.right:
                precessor = precessor.right
            # 交换删除
            cur.val = precessor.val
            cur.left = self.deleteNode(cur.left, cur.val)
        else:
            # 右边不为空，找到后继节点
            successor = cur.right
            while successor.left:
                successor = successor.left
            # 交换删除
            cur.val = successor.val
            cur.right = self.deleteNode(cur.right, cur.val)
        
        return dummy.left