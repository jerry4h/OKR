# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        curr = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            curr = curr.next
        
        start = curr.next
        for _ in range(n-m):
            # tmp相当于一个独立的节点，插在链表中间，没人指向它
            tmp = start.next
            start.next = tmp.next
            # tmp相当于一个独立的节点，插在链表中间
            tmp.next = curr.next
            curr.next = tmp
        
        return dummy.next
