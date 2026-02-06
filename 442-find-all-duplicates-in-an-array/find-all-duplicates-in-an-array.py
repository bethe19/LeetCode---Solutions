class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map = Counter(nums)
        result = []
        for i,j in map.items():
            if j > 1:
                result.append(i)
        return result
        