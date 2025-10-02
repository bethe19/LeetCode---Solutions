class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for char in s + t:
            res ^= ord(char)
        return chr(res)  
