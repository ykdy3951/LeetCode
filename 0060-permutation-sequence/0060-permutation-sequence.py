class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i + 1 for i in range(n)]
        for _ in range(k-1):
            i = n - 1
            while arr[i - 1] > arr[i]:
                i -= 1
            j = n - 1
            while arr[i - 1] > arr[j]:
                j -= 1
            arr[i - 1], arr[j] = arr[j], arr[i - 1]
            arr[i:n] = arr[n-1:i-1:-1]
        return "".join(map(str, arr))