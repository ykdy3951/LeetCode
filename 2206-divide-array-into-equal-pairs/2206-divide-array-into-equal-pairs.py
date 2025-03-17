class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        for i in d.values():
            if i % 2 != 0:
                return False
        return True