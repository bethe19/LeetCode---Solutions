class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2== 0:
            i = 1
            while len(result) != n:
                result.append(i)
                result.append(-i)
                i+=1
        if n % 2 != 0:
            return [0] + self.sumZero(n-1)
        return result