from math import sqrt
from collections import deque
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        d = deque()
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, right + 1):
            if not is_prime[i]:
                continue
            if left <= i:
                d.append(i)
            for j in range(i * i, right + 1, i):
                is_prime[j] = False

        ans = [-1, -1]
        if not len(d):
            return ans
        gap = float('inf')
        last = d.popleft()
        while d:
            temp = d.popleft()
            if gap > (temp - last):
                ans = [last, temp]
                gap = temp - last
            last = temp
        return ans
