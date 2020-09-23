[LC23](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    struct Status {
        int val;
        ListNode *ptr;
        bool operator < (const Status& rhs) const {
            // 默认大顶堆，所以这里重载反了
            return val > rhs.val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // 默认大根堆
        priority_queue <Status> q;
        for(ListNode* node : lists){
            if (node) q.push({node->val, node});
        }
        ListNode head, *tail = &head;
        while (!q.empty()){
            // 注意优先队列的pop
            Status p=q.top(); q.pop();
            tail->next = p.ptr; tail = tail->next;
            if (p.ptr->next) q.push({p.ptr->next->val, p.ptr->next});
        }
        // head不是指针类型，则.；指针类型则->
        return head.next;
    }
};
```