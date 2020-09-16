# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        head.next.next = self.swapPairs(head.next.next)
        # 不需要交换空间
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        head = tmp

        return head
        