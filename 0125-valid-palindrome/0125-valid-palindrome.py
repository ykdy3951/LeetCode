class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(lambda x: x.isalpha() or x.isdigit(), s)).lower()
        return s == s[::-1]