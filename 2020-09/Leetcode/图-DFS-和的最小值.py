
#          0
#        /   \
#      1 ---- 2
#     / |    | \
#    3  |    |  4
#     \ |    | /
#      5 ---- 6
#       \    /
#          7
# 把{1,2,3}放到上面各个序号的格子里，要求相邻的格子的数值不相同，求8个格子总和的最小值
# 这里思路是DFS+回溯法。DFS的是以序号做顺序。

graph = {
    0: [1, 2],
    1: [0, 2, 3, 5],
    2: [0, 1, 4, 6],
    3: [1, 5],
    4: [2, 6],
    5: [1, 3, 6, 7],
    6: [2, 4, 5, 7],
    7: [5, 6]
}
min_num = [float("inf")]
ans = []
def dfs(idx, tmp, tsum):
    """给定一个idx
    """
    if idx == 7:
        ans.append(tmp[:])
        min_num[0] = min(min_num[0], tsum)
        if tsum == 14:
            print(tmp)
        return
    
    # idx+1的序号选三个数尝试
    idx_next = idx+1
    for num in range(1, 4): # 1 2 3
        status = True
        # 判断idx+1能不能走：相邻且有数的，和当前num都不相同
        for neighbor in graph[idx_next]:
            if neighbor > idx:
                continue
            if tmp[neighbor] == num:
                status = False
                break

        if status:
            tmp.append(num)
            dfs(idx_next, tmp, tsum+num)
            tmp.pop()

dfs(idx=-1, tmp=[], tsum=0)
print(ans)
print(min_num)
    