# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        fn, fn_1 = 1, 0
        for i in range(N-1):
            fn, fn_1 = fn+fn_1, fn
        return fn
