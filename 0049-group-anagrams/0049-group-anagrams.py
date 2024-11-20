from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            s = defaultdict(int)
            for j in i:
                s[j] += 1
            k = ""
            for key in sorted(list(s.keys())):
                k += key + str(s[key])
            d[k].append(i)
        ans = []
        for i in d.values():
            ans.append(i)
        return ans
        