from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for key in d:
            if d[key] == 1:
                return key