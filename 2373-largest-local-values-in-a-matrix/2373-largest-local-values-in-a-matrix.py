class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid[0])
        target = n - 2
        ans = [[0] * target for _ in range(target)]
        for i in range(target):
            for j in range(target):
                max_val = max(
                    grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
                )
                ans[i][j] = max_val
        return ans