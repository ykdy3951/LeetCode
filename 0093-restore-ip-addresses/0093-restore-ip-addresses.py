class Solution:
    def __init__(self):
        self.ans = []
    def recursive(self, s : str, idx : int, temp : list, part : str):
        if len(temp) > 3:
            return
        if idx >= len(s):
            # Check temp list
            temp.append(part)
            if len(temp) == 4:
                self.ans.append(".".join(temp))
            return
        
        if len(temp) + 1 <= 4:
            self.recursive(s, idx + 1, temp + [part], s[idx])
        
        # 1. increase this part
        if int(part + s[idx]) <= 255 and not (len(part) + 1 > 1 and int(part + s[idx]) == 0) and part[0] != "0":
            self.recursive(s, idx + 1, temp, part + s[idx])
        
        
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.recursive(s, 1, [], s[0])
        return self.ans