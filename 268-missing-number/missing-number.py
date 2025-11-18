class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        archimeticSum = n*(n+1)//2
        return archimeticSum - sum(nums)