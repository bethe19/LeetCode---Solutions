class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat[0]) 
        for i in range(n):
            if i != n-i-1: sum += mat[i][i] + mat[i][n-i-1]
            else: sum += mat[i][i]
        return sum
