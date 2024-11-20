class Solution:
    def backtracking(self, size = 0, result: List[int] = []):
        if size == self.n:
            self.ans.append(result)
            return
        
        for i in range(self.n):
            if self.vst[i]:
                continue
            
            if i > 0 and self.nums[i] == self.nums[i - 1] and not self.vst[i - 1]:
                continue
            
            self.vst[i] = True
            self.backtracking(size + 1, result + [self.nums[i]])
            self.vst[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.n = len(nums)
        self.nums = nums
        self.vst = [False] * self.n
        self.backtracking()
        return self.ans