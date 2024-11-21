class Solution:
    def backtracking(self, res = [], start_idx = 0):
        self.ans.append(res)

        for i in range(start_idx, self.n):
            if self.vst[i]:
                continue

            if i > 0 and self.nums[i] == self.nums[i-1] and not self.vst[i - 1]:
                continue

            self.vst[i] = True
            self.backtracking(res + [self.nums[i]], i + 1)
            self.vst[i] = False


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.n = len(nums)
        self.vst = [False] * self.n
        self.ans = []
        self.backtracking()
        return self.ans