# [567] 字符串的排列
#

# @lc code=start
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = collections.Counter(s1)
        dict_window = collections.defaultdict(int)
        num_matched = 0
        
        i, j = 0, 0
        # 注意优先走j
        while j < len(s2):
            cj = s2[j]
            dict_window[cj] += 1
            # 注意两种情况的判断
            if cj in dict1:
                if dict_window[cj] == dict1[cj]:
                    num_matched += 1
                if dict_window[cj] == dict1[cj]+1:
                    num_matched -= 1
            
            while j-i+1 > len(s1):
                ci = s2[i]
                dict_window[ci] -= 1
                # 注意两种情况的判断
                if ci in dict1:
                    if dict_window[ci] == dict1[ci]:
                        num_matched += 1
                    if dict_window[ci] == dict1[ci]-1:
                        num_matched -= 1
                # end
                i += 1
            if j-i+1 == len(s1) and num_matched == len(dict1):
                return True
            
            # end
            j += 1
        return False
