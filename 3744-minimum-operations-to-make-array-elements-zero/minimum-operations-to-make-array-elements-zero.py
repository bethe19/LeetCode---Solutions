class Solution:
    def prefix(self, m: int) -> int:
        if m < 1:
            return 0
        k = int(log(m,4))
        pow4 = 4**k
        if k == 0:
            return 0
        sum1 = (4 + pow4 * (3 * k - 4)) // 3
        last = k * (m - pow4 + 1)
        return sum1 + last
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            total = (r - l + 1) + self.prefix(r) - self.prefix(l - 1)
            ops = (total + 1) // 2
            ans += ops
        return ans