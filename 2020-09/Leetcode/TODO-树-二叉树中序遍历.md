[LC94](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

迭代写法
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        stack = []
        def insert(node):
            stack.append(node)
            while node.left:
                stack.append(node.left)
                node = node.left
        insert(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                insert(node.right)
        return ans

```

TODO: moris中序遍历，能改变二叉树的情况下，把空间复杂度降到O(n)
[moris](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/)
- 把末端节点连接到根节点（找一个捷径）
- 只用一个指针x的情况下，中序遍历所有的节点