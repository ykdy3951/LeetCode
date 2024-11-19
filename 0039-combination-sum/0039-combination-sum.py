class Solution:
    def backtracking(self, sum_val: int, ans_cand: List[int], last_idx: int) -> List[int]:
        if sum_val == self.target:
            self.ans.append(ans_cand)
            return

        for i in range(last_idx, self.n):
            val = self.candidates[i]
            if sum_val + val > self.target:
                break
            
            self.backtracking(sum_val + val, ans_cand + [val], i)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.candidates = candidates
        self.target = target
        self.ans = []
        self.n = len(candidates)

        self.backtracking(0, [], 0)
        return self.ans