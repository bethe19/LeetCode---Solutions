class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for _ in range(9)]
        cols = [[0]*9 for _ in range(9)]
        boxes = [[0]*9 for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                num = int(val) - 1
                if rows[r][num] or cols[c][num] or boxes[(r//3)*3 + (c//3)][num]:
                    return False
                rows[r][num] = cols[c][num] = boxes[(r//3)*3 + (c//3)][num] = 1
        return True