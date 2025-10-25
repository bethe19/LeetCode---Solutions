class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        remainder = n%7
        sum = 0
        for i in range(weeks):
            sum += (i+1 + 7+i)*7//2
        if remainder:
            sum += (weeks + 1 +weeks + remainder) * remainder//2
        return int(sum)
            