from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        answer = defaultdict(int)
        for i in nums1:
            answer[i[0]] += i[1]
        for i in nums2:
            answer[i[0]] += i[1]

        answerList = []
        for i in sorted(list(answer.keys())):
            answerList.append([i, answer[i]])

        return answerList