# [1314] 矩阵区域和
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or len(mat[0]) == 0:
            return False

        m, n = len(mat), len(mat[0])
        # 前缀和：保存[i,j]到[0,0]的矩阵和
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # 更新 dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]

        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # dp的序号得+1，x1,y1得-1，细节需要注意
                x1, x2 = max(0, i-K), min(m, i+K+1)
                y1, y2 = max(0, j-K), min(n, j+K+1)
                ans[i][j] = dp[x2][y2] + dp[x1][y1] - dp[x1][y2] - dp[x2][y1]
        return ans
