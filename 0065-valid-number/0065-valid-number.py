class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            s = s.lower()
            for i in range(26):
                if chr(i+97) == 'e':
                    continue
                if chr(i+97) in s:
                    return False
            float(s)
        except:
            return False
        return True