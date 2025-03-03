class Solution:
    def __init__(self):
        self.ans = []
        self.chkBoard = [[[False] * 9 for _ in range(9)] for _ in range(3)]

    def backtracking(self, board: List[List[str]], leftIdx: List[List[int]]):
        if not len(leftIdx):
            self.ans = board
            return True

        for i in range(9):
            r, c = leftIdx[0][0], leftIdx[0][1]
            if self.chkBoard[0][r][i] or self.chkBoard[1][c][i] or self.chkBoard[2][r // 3 * 3 + c // 3][i]:
                continue 
            board[r][c] = str(i + 1)
            self.chkBoard[0][r][i] = True
            self.chkBoard[1][c][i] = True
            self.chkBoard[2][r // 3 * 3 + c // 3][i] = True
            if self.backtracking(board, leftIdx[1:]):
                return True
            self.chkBoard[0][r][i] = False
            self.chkBoard[1][c][i] = False
            self.chkBoard[2][r // 3 * 3 + c // 3][i] = False
        
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        leftIdx = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    leftIdx.append([i, j])
                    continue
                num = int(board[i][j])
                self.chkBoard[0][i][num - 1] = True
                self.chkBoard[1][j][num - 1] = True
                self.chkBoard[2][i // 3 * 3 + j // 3][num - 1] = True

        self.backtracking(board, leftIdx)