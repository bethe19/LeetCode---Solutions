class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # # bruteforce..
        # i = 1
        # while k > 0:
        #     if i not in arr:
        #         k -= 1
        #     i += 1
        # return i-1

        left,right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right)//2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
         
        return k + left
