class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dictionary = {i: 1 for i in range(1, n ** 2 + 1)}
        ans = [0, 0]
        for i in grid:
            for j in i:
                dictionary[j] -= 1
                if dictionary[j] < 0:
                    ans[0] = j

        for i, j in dictionary.items():
            if j == 1:
                ans[-1] = i
                break
        
        return ans