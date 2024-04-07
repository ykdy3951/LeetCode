class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        m = {}

        for i in range(len(nums)):
            if target - nums[i] in m:
                output.append(i)
                output.append(m[target-nums[i]])
                break
            else:
                m[nums[i]] = i
                
        return output