class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        b = set()
        for i, j in friendships:
            f = any(k in languages[i-1] for k in languages[j-1])
            if not f:
                b.add(i)
                b.add(j)
        
        result = float('inf')

        for i in range(1,n+1):
            count = 0
            for j in b:
                if i in languages[j-1]:
                    count += 1
            k = len(b) - count
            result = min(result, k)
        
        return result
        