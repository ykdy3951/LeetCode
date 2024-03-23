import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while p.count("**"):
            p = p.replace("**", "*", 1)
        return re.fullmatch(p, s)