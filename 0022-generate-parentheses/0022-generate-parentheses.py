class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(o, c, s):
            if len(s) == n * 2:
                ans.append(s)
            
            if o < n:
                dfs(o+1, c, s + '(')
            
            if c < o:
                dfs(o, c + 1, s + ')')

        dfs(0,0,"")
        return ans
                