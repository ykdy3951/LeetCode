class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diag = [[0 for _ in range(2*n)] for _ in range(2)]
        chk = [0] * n
        ans = []
        def return_board(l):
            ret = []
            for i in range(n):
                s = ''
                for j in range(n):
                    s += '.' if j != l[i] else 'Q'
                ret.append(s)
            return ret

        def backtracking(l, depth = 0):
            if depth == n:
                ans.append(return_board(l))
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
        return ans