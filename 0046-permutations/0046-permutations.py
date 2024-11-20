class Solution:
    def backtracking(self, size: int = 0, res: List[int] = []):
        if size == self.n:
            self.ans.append(res)
            return
        
        for i in range(self.n):
            if self.vst[i]:
                continue
            
            self.vst[i] = True
            self.backtracking(size + 1, res + [self.nums[i]])
            self.vst[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.vst = [False] * self.n
        self.ans = []
        self.backtracking()
        return self.ans

        