class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        maxlength = 0
        left  = 0
        right = 0
        while right < len(s):
            while s[right] in s[left:right]:
                left += 1
            
            maxlength = max(maxlength, right - left + 1)

            right += 1
        return maxlength
