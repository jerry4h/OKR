# [721] 账户合并
#

# @lc code=start
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        father = [i for i in range(n)]
        id2email = collections.defaultdict(set)
        email2id = dict()

        def find(u):
            if father[u] == u:
                return u
            else:
                return find(father[u])
        
        def union(u, v):
            fu = find(u)
            fv = find(v)
            if fu == fv:
                return True
            else:
                father[fu] = fv
                return False

        # 账户名合并
        for i, rec in enumerate(accounts):
            name = rec[0]
            for email in rec[1:]:
                if email in email2id:
                    union(i, email2id[email])
                else:
                    email2id[email] = i
        # 邮箱融合账户名
        for i, rec in enumerate(accounts):
            root = find(i)
            for email in rec[1:]:
                id2email[root].add(email)
        ans = []
        for key, value in id2email.items():
            line = [i for i in value]
            line.sort()
            ans.append([accounts[key][0]]+line)
        return ans
