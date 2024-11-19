class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        s = self.countAndSay(n - 1)
        
        ret = ""
        tmp = s[0]
        cnt = 1
        for i in s[1:]:
            if i != tmp:
                ret += str(cnt) + tmp
                tmp = i
                cnt = 1
            else:
                cnt += 1
        ret += str(cnt) + tmp
        return ret
                