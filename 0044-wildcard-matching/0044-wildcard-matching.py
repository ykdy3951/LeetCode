class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, idx1, idx2, s, p):
        if idx1 < 0 and idx2 < 0:
            return True
        if idx2 < 0 and idx1 >= 0:
            return False
        if idx1 < 0 and idx2 >= 0:
            for i in range(idx2 + 1):
                if p[i] != '*':
                    return False
            return True
        if self.dp[idx1][idx2] != -1:
            return self.dp[idx1][idx2] == 1


        if s[idx1] == p[idx2] or p[idx2] == '?':
            self.dp[idx1][idx2] = int(self.solve(idx1 - 1, idx2 - 1, s, p))
        
        elif p[idx2] == '*':
            self.dp[idx1][idx2] = int(self.solve(idx1 - 1, idx2, s, p) or self.solve(idx1, idx2 - 1, s, p))

        else:
            self.dp[idx1][idx2] = 0
        
        return self.dp[idx1][idx2] == 1

    def isMatch(self, s: str, p: str) -> bool:
        sidx, pidx = len(s) - 1, len(p) - 1
        self.dp = [[-1 for _ in range(pidx + 1)] for _ in range(sidx + 1)]
        return self.solve(sidx, pidx, s, p)