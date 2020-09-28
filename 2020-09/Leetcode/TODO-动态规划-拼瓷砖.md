
拼多多笔试题。

对N列M行的空间用1x1, 2x2的瓷砖去拼，有多少种拼法。
- N是个大数
- 1<=M<=5

这个代码5%（只过了M=1），不知道原因，难道全部都是大数，必须要写成递归的形式？

```python
import sys
# 注意排除重复的dp[2]-dp[1]
dic = {
    2: 1,
    3: 2,
    4: 4,
    5: 7,
}

def getAns(N, M):
    rate = dic[M]
    dp, dp_1, dp_2 = rate+1, 1, 0
    for i in range(N-2):
        dp_1, dp_2 = dp, dp_1
        dp = dp_1 + dp_2 * rate
    return dp

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, M = list(map(int, line.split()))
    if M == 1:
        print(1)
    else:
        ans = getAns(N, M)
        print(ans)
```