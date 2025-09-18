class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(current, o, c):
            if len(current) == 2*n:
                result.append(current)
                return
            if o < n:
                gen(current + '(',o + 1, c)
            if c < o:
                gen(current + ")", o, c + 1)
        gen('',0,0)
        return result
        