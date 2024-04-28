class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        arr = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = [0] + arr[i-1] + [0]
            p = []
            for j in range(len(tmp)-1):
                p.append(tmp[j] + tmp[j+1])
            arr.append(p)
        return arr
            