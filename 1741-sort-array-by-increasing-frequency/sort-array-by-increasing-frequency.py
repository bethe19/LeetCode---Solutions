class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        result = sorted(nums, key=lambda x: (map[x], -x))
        return result