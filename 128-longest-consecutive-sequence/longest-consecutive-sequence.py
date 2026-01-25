class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        arr = set(nums)
        streak = 0

        for i in arr:
            if (i - 1) not in arr:
                curr = i
                curr_s = 1
                while (curr + 1) in arr:
                    curr += 1
                    curr_s += 1
                streak = max(streak,curr_s)
        return streak