class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        while l < r:
            if s[l] not in vowel:
                l += 1
            if s[r] not in vowel:
                r -= 1
            if s[r] in vowel and s[l] in vowel:
                s[l], s[r] = s[r], s[l]
                r -=1
                l +=1
        return ("").join(s)