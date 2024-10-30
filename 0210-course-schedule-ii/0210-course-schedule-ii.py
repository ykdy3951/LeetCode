from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            x, y = prerequisite
            graph[y].append(x)
            
        childrens = [0] * numCourses
        for prerequisite in prerequisites:
            x, y = prerequisite
            childrens[x] += 1

        d = deque()
        for i in range(numCourses):
            if not childrens[i]:
                d.append(i)

        ans = []
        while d:
            now = d.popleft()
            ans.append(now)

            for nxt in graph[now]:
                childrens[nxt] -= 1
                if not childrens[nxt]:
                    d.append(nxt)
        
        if len(ans) < numCourses:
            return []
        
        return ans