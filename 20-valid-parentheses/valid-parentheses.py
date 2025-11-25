class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack and mapping[i] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack

