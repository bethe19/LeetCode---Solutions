class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums = [nums[0]] + [nums[i] for i in range(1, len(nums)) if nums[i] != nums[i-1]]
        count = 0 
        for i in range(1,len(nums)-1):
            if nums[i-1] > nums [i] and nums[i+1] > nums[i] or nums[i-1] < nums [i] and nums[i+1] < nums[i]:
                count += 1

        return count