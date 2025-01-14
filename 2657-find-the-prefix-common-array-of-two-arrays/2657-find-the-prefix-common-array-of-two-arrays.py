class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        output = []
        bitA = 0; bitB = 0
        for i in range(len(A)):
            bitA |= 1 << A[i]; bitB |= 1 << B[i]
            cnt = bin(bitA & bitB).count('1')
            output.append(cnt)
        return output