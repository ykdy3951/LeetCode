class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        ans = []
        is_used = False

        while i < n:
            if not is_used and newInterval[0] < intervals[i][0]:
                now = newInterval
                nxt_i = i
                is_used = True
            else:
                now = intervals[i]
                nxt_i = i + 1
        
            if not len(ans):
                ans.append(now)
            else:
                if ans[-1][1] >= now[0]:
                    ans[-1][1] = max(ans[-1][1], now[1])
                else:
                    ans.append(now)
            
            i = nxt_i

        if not is_used:
            now = newInterval
            if len(ans) > 0 and ans[-1][1] >= now[0]:
                ans[-1][1] = max(ans[-1][1], now[1])
            else:
                ans.append(now)
        
        return ans