
> 有n个人，抽出k个，每个人的不同能力值为an，找到最大的能力值。其中n-1组人有矛盾，抽取的情况里必须分开，矛盾用pair来表示

这种题怎么入手？

```python
import sys

def getAns(n, k, an, pairs):
    an.sort()
    print(sum(an[-k:]))

if __name__ == "__main__":
    # 读取第一行的n
    K = int(sys.stdin.readline().strip())
    for _ in range(K):
        line = sys.stdin.readline().strip()
        n, k = list(map(int, line.split()))
        line = sys.stdin.readline().strip()
        an = list(map(int, line.split()))
        pairs = []
        for _ in range(n-1):
            line = sys.stdin.readline().strip()
            pairs.append(list(map(int, line.split())))
        getAns(n, k, an, pairs)
```