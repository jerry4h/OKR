# [210] 课程表 II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        VISITED = 0
        DISCOVERING = 1
        NOT_VISITED = 2

        # 依赖关系
        dependences = collections.defaultdict(list)
        for course, pre in prerequisites:
            dependences[course].append(pre)
        # 输出结果栈
        stack = []
        # 状态
        status = [NOT_VISITED for _ in range(numCourses)]

        def dfs(course):
            status[course] = DISCOVERING
            for i in dependences[course]:
                if status[i]==DISCOVERING or (status[i]==NOT_VISITED and not dfs(i)):
                    return False
            status[course] = VISITED
            # 从上往下找。随机一个节点，不需要上面的紧贴在后面，但必须满足下面的立即在前面
            stack.append(course)
            return True

        for i in range(numCourses):
            if status[i] == NOT_VISITED and not dfs(i):
                return []
        return stack
    