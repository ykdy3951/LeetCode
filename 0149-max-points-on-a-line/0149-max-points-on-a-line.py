from collections import defaultdict
from math import ceil
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        n = len(points)

        if n == 1:
            return 1
        points.sort()
        for i in range(n-1):
            for j in range(i+1, n):
                a,b = points[i], points[j]
                if b[0] == a[0]:
                    slope_p, slope_c, x_in, y_in = 0, 0, a[0], 0
                else:
                    slope_p, slope_c = b[1] - a[1], b[0] - a[0]
                    g = gcd(slope_p, slope_c)
                    slope_p, slope_c = slope_p // g, slope_c // g
                    x_in = 0
                    y_in = slope_p * a[0] - a[1] * slope_c
                
                d[(slope_p, slope_c, y_in, x_in)]+=1
        print(d)
        return int(ceil(sqrt(max(d.values())*2)))