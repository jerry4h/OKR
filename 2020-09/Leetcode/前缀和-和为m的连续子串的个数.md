
依图一面题

a=[0, 1, 1, 0, 1], m = 2

满足条件有：

0 1 1

0 1 1 0

1 1

1 1 0

1 0 1

rtn=5

```python
import collections
def solution(a, m):
    if not a:
        return 0
    dic = collections.defaultdict(list)
    # 前缀和的初始化
    dic[0].append(-1)
    sumi = 0
    ans = 0
    for i, num in enumerate(a):
        sumi += num
        tgt = sumi - m
        ans += len(dic[tgt])
        dic[sumi].append(i)
    return ans
```