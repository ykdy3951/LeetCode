from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        list_length = len(words)
        word_length = len(words[0])
        total_length = list_length * word_length

        words_count = defaultdict(int)
        for word in words:
            words_count[word] += 1
        
        ans = []
        for i in range(len(s) - total_length + 1):
            cnt = defaultdict(int)
            for j in range(i, total_length + i, word_length):
                word = s[j:j+word_length]
                if word in words_count:
                    cnt[word] += 1
                    if cnt[word] > words_count[word]:
                        break
                else:
                    break
            else:
                ans.append(i)
        return ans
                