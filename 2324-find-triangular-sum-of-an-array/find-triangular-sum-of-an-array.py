class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newNums = []

        i = 0
        while True:
            if len(nums) == 1:
                break
            if i+1 == len(nums):
                nums = newNums
                newNums = []
                i = 0
                continue
            sum = ( nums[i] + nums[i+1] ) % 10
            newNums.append(sum)
            i += 1
        return nums[0]