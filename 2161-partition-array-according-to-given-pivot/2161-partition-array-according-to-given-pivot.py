class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cnt = 0
        left = []
        right = []
        for i in nums:
            if pivot < i:
                right.append(i)
            elif pivot > i:
                left.append(i)
            else:
                cnt += 1
        return left + [pivot] * cnt + right