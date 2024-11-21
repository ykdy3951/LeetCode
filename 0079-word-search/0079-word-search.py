from collections import deque
class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = False

    def backtracking(self, x, y, cnt = 0):
        if self.ans:
            return 
        
        if cnt == len(self.word):
            self.ans = True
            return

        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]

            if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m or self.vst[nx][ny]:
                continue

            if self.word[cnt] != self.board[nx][ny]:
                continue

            self.vst[nx][ny] = True
            self.backtracking(nx, ny, cnt + 1)
            self.vst[nx][ny] = False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n, self.m = len(board), len(board[0])
        self.word = word
        self.vst = [[False] * self.m for _ in range(self.n)]
        self.board = board
        
        d = deque()
        for i in range(self.n):
            for j in range(self.m):
                if word[0] == board[i][j]:
                    d.append([i, j, 1])

        while d:
            x, y, cnt = d.pop()
            self.vst[x][y] = True
            self.backtracking(x, y, cnt)
            self.vst[x][y] = False
            if self.ans:
                return True

        return False