class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        
        for i in range(len(columnTitle)):
            s = columnTitle[::-1][i]
            number += (ord(s) - 64) * (26 ** i)
            
        return number
