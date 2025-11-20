class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in my_map:
                return [my_map[candidate],i]
            my_map[nums[i]] = i