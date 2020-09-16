# [3] 无重复字符的最长子串
# 这题细节很多，还是得小心留意

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        last_index = {}
        l, max_len = 0, 0
        for r in range(n):
            cr = s[r]
            if cr in last_index and last_index[cr] >= l:
                max_len = max(max_len, r-l)
                l = last_index[cr] + 1
            last_index[cr] = r
        
        # 最长的位置可能没有重复
        return max(max_len, n-l)
