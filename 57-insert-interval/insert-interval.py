class Solution:
    def insert(self, a: List[List[int]], n: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(a) and a[i][1] < n[0]:
            result.append(a[i])
            i += 1
        while i < len(a) and a[i][0] <= n[1]:
            n[0] = min(n[0], a[i][0])
            n[1] = max(n[1], a[i][1])
            i += 1
        result.append(n)

        while i < len(a):
            result.append(a[i])
            i += 1
        
        return result