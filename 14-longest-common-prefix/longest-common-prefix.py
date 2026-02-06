class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        for i in strs:
            l = min(len(i),l)
        prefix = ''
        for i in range(l):
            p = True
            k = strs[0][i]
            for j in range (1,len(strs)):
                if strs[j][i] != k:
                    p = False
                    break
            if p: prefix += k
            else: break
        return prefix
