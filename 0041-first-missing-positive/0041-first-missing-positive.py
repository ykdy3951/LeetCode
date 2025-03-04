class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x : x > 0, nums))
        for i in nums:
            idx = abs(i) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1