class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = nums.copy()
        for i in range(1,len(nums)):
            sum[i] += sum[i-1]
        for i in range(len(nums)):
            if sum[i] - nums[i] == sum[-1] - sum[i]:
                return i
        return -1
