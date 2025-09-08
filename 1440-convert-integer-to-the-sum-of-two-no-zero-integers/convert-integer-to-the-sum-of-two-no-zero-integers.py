class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        n = n-1
        s = str(n)
        t = str(i)
        while '0' in s or '0' in t:
            n -= 1
            i += 1
            s = str(n)
            t = str(i)
        return [i,n]