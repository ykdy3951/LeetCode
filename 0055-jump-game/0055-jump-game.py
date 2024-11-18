"""
input : List[int]
initial : idx = 0
the value of array : maximum jump length
determine whether i can visit the end of array
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return target == 0
        