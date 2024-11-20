class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        x, y = 0, 0
        dx, dy = 0, 1
        val = 1
        vst = [[False] * n for _ in range(n)]

        while val <= n * n:
            matrix[x][y] = val
            vst[x][y] = True

            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or vst[nx][ny]:
                dx, dy = dy, -dx

            x, y = x + dx, y + dy
            val += 1
        return matrix