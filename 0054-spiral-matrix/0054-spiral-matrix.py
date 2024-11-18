class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        vst = [[0] * n for _ in range(m)]
        x, y = 0, 0
        dx, dy = 0, 1
        while cnt < m * n:
            ans.append(matrix[x][y])
            vst[x][y] = True
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                dx, dy = dy, -dx
            elif vst[nx][ny]:
                dx, dy = dy, -dx
            
            x, y = x + dx, y + dy
            cnt += 1
        return ans