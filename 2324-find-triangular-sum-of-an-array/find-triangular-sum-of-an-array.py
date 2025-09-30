class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = []
        while len(nums) > 1:
            for i in range(1, len(nums)):
                s = nums[i] + nums[i-1]
                if s >= 10:
                    s -= 10
                result.append(s)
            nums = result
            result = []
        return nums[0]