class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        opsArr = []

        for i in range(len(boxes)):
            ops = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    ops += abs(i-j)
            opsArr.append(ops)
        
        return opsArr