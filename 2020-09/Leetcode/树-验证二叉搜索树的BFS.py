
# 给定一个序列，判断是否为一个二叉搜索树的BFS。

import collections

def bst_bfs(A):
    print(A)
    if not A:
        return True
    N = len(A)
    # 把运行顺序压缩成单序列了。
    interval = collections.deque([(float("-inf"), A[0]), (A[0], float("inf"))])
    for ai in A[1:]:
        while interval:
            lower, upper = interval.popleft()
            # 一定得找到一个满足条件的范围
            # 否则这个数越界，不是二叉搜索树。
            if lower < ai < upper:
                interval.append((lower, ai))
                interval.append((ai, upper))
                break
        if not interval:
            return False
    return True
        
ans = bst_bfs([10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 12])
print(ans)
ans = bst_bfs([10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 7])
print(ans)