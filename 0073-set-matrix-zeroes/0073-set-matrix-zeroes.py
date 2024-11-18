class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = set()
        # cols = set()
        rows = 0
        cols = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # rows.add(i)
                    # cols.add(j)
                    rows |= 1 << i
                    cols |= 1 << j
        
        # for i in rows:
        #     for j in range(m):
        #         matrix[i][j] = 0
        # for j in cols:
        #     for i in range(n):
        #         matrix[i][j] = 0
        i = 0
        while rows:
            val = rows % 2
            if val:
                for j in range(m):
                    matrix[i][j] = 0
            rows >>= 1
            i += 1
        j = 0
        while cols:
            val = cols % 2
            if val:
                for i in range(n):
                    matrix[i][j] = 0
            cols >>= 1
            j += 1