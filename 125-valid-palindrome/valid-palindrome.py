class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ''
        for i in s:
            if i < 'a' or i > 'z':
                if i >= '0' and i <= '9':
                    t += i
                continue
            t += i
        
        if  t == t[::-1]:
            return True
        return False
