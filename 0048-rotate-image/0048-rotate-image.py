class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        dx, dy = -1, 0
        odx, ody = 0, 1
        x, y = n-1, 0
        ox, oy = 0, 0
        ans = [[0] * n for _ in range(n)]
        vst = [[False] * n for _ in range(n)]
        while i < n * n:
            ans[ox][oy] = matrix[x][y]
            vst[x][y] = True

            nx, ny = x + dx, y + dy
            nox, noy = ox + odx, oy + ody

            if nx < 0 or nx >= n or ny < 0 or ny >= n or vst[nx][ny]:
                dx, dy = dy, -dx
                odx, ody = ody, -odx

            x, y = x + dx, y + dy
            ox, oy = ox + odx, oy + ody
            i += 1
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]