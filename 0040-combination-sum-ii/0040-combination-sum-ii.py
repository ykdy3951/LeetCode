class Solution:
    def backtracking(self, value : int = 0, result : List[int] = [], start_idx: int = 0):
        if value == self.target:
            self.ans.append(result)
            return
        
        for i in range(start_idx, self.n):
            now = self.candidates[i]
            nval = now + value

            if nval > self.target:
                return 

            if i - start_idx > 0 and now == self.candidates[i - 1]:
                continue
            
            self.backtracking(nval, result + [now], i + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.n = len(candidates)
        self.ans = []

        self.backtracking()
        return self.ans