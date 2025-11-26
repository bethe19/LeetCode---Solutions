class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == "../":
                depth = max(0, depth - 1)
            elif op == "./":
                continue
            else:
                depth += 1
        return depth