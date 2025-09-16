class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            if gcd(nums[i-1],nums[i]) > 1:
                nums[i] = lcm(nums[i-1],nums[i])
                nums.pop(i-1)
                i = max(1, i-1)
            else:
                i += 1

        return nums