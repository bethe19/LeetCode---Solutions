class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            if nums[right] == 0:
                right += 1
            elif nums[left] != 0:
                left += 1
                right = left + 1
            else:
                nums[left],nums[right] = nums[right], nums[left]

