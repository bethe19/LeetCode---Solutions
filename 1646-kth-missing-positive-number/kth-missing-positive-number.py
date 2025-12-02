class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        i = 0
        arr = set(arr)
        while count < k:
            i += 1
            if i not in arr:
                count += 1
        
        return i