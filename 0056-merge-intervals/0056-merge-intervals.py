from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d = deque()

        n = len(intervals)
        intervals.sort()

        d.append(intervals[0])
        for i in range(1, n):
            top = d.pop()
            if top[1] >= intervals[i][0]:
                d.append([top[0], max(top[1], intervals[i][1])])
            else:
                d.append(top)
                d.append(intervals[i])
        
        ans = []
        while d:
            ans.append(d.pop())

        return ans