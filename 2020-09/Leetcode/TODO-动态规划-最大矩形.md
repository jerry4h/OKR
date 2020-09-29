[LC85](https://leetcode-cn.com/problems/maximal-rectangle/)

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

> 输入\
> [\
>   ["1","0","1","0","0"],\
>   ["1","0","1","1","1"],\
>   ["1","1","1","1","1"],\
>   ["1","0","0","1","0"]\
> ]\
> 输出: 6


```python
# 前缀和：TLE
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        sumij = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                sumij[i][j] = int(matrix[i-1][j-1]) + sumij[i-1][j] + sumij[i][j-1] - sumij[i-1][j-1]

        def gen(i, j):
            for a in range(i, n):
                for b in range(j, m):
                    yield (a, b)
        ans = 0
        for i in range(n):
            for j in range(m):
                for a, b in gen(i, j):
                    # a, b, i, j都为闭区间
                    h, w = max(1, a-i+1), max(1, b-j+1)
                    area = h * w
                    tmp = sumij[a+1][b+1] - sumij[a+1][j] - sumij[i][b+1] + sumij[i][j]
                    if tmp == area:
                        ans = max(tmp, ans)
                        break
        return ans
```