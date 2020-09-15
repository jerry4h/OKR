
# [743] 网络延迟时间
#

# @lc code=start

# Dijkstra's Algorithm(类似BFS，每次找到一个最小的BFS节点)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

# 优先级队列（堆），其实是优化查找时间
import heapq
import collections
class Solution2:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # 优先级队列
        pq = [(0, K)]
        dist = {}
        while pq:
            dis, idx = heapq.heappop(pq)
            if idx in dist:
                continue
            dist[idx] = dis
            for u, w in graph[idx]:
                if u not in dist:
                    heapq.heappush(pq, (dis+w, u))
        return max(dist.values()) if len(dist)==N else -1