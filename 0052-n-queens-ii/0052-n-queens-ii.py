class Solution:
    def totalNQueens(self, n: int) -> int:
        diag = [[0 for _ in range(2*n)] for _ in range(2)]
        chk = [0] * n
        ans = []

        def backtracking(l, depth = 0):
            if depth == n:
                ans.append(l)
                return

            for i in range(n):
                if chk[i] or diag[0][i + depth] or diag[1][n - depth + i - 1]:
                    continue
                chk[i] = diag[0][i + depth] = diag[1][n-depth+i-1] = True
                l.append(i)
                backtracking(l, depth + 1)
                l.pop()
                chk[i] = diag[0][i + depth] = diag[1][n-depth+i-1] = False


        backtracking([])
        return len(ans)