class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        ans = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i + 1)
            else:
                stack.pop()
                if not stack:
                    stack.append(i + 1)
                else:
                    ans = max(ans, i + 1 - stack[-1])

        return ans