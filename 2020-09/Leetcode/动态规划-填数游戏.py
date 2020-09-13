# 给三个数n,k,d(1<=d<=n<=1000)
# 给出所有可能的: _+_+_+...+_=n 的可能公式。
# 公式里的每个数必须大于等于1，小于等于k，填入数的最大值必须大于等于d

# dp[n][m] 表示和为n，方程中最大值为m的总方程个数
# 转移方程：dp[n][m]=dp[n-m][m]+dp[n-m][m-1]+...+dp[n-m][1]
# 初始状态：

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]]

for i in range(n+1):
    for j in range(k+1):
        # 最大值等于和：只有一种方案
        if i == j:
            dp[i][j] = 1
        # j大于等于1，小于等于k 已满足
        # 最大值必须大于等于d
        if j < d:
            dp[i][j] = 0

# TODO: 待验证
