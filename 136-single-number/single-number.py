class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for i,j in nums.items():
            if j == 1: return i