from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = deque()
        for i in tokens:
            if i in "+-*/":
                f, s = d.pop(), d.pop()
                d.append(str(int(eval(s + i + f))))
            else:
                d.append(i)
        return int(d.pop())