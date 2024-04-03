from itertools import combinations as comb
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        l = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = list(l[int(digits[0])-2])
        for i in digits[1:]:
            temp = []
            for j in output:
                for k in list(l[int(i)-2]):
                    temp.append(j+k)
            output = temp
        return output