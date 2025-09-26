class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for k in range(len(nums)-1, 1, -1):
            l,r = 0, k-1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count