from itertools import permutations

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        decreasing_index = len(nums) - 2
        while decreasing_index >= 0 and nums[decreasing_index] >= nums[decreasing_index + 1]:
            decreasing_index -= 1

        if decreasing_index == -1:
            nums.reverse()
            return
        
        for i in range(len(nums) - 1, decreasing_index, -1):
            if nums[i] > nums[decreasing_index]:
                nums[i], nums[decreasing_index] = nums[decreasing_index], nums[i]
                break
        
        nums[decreasing_index + 1:] = nums[decreasing_index + 1:][::-1]
