class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums = sorted(nums, key=cmp_to_key(compare))
        if nums[0] == '0':
            return '0'
        result = ""
        for i in nums:
            result += i
        return result