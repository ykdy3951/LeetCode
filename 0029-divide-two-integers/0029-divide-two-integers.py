class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return max(min(2**31-1, int(dividend / divisor)), -2**31)