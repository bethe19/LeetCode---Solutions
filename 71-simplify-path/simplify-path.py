class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for i in path:
            if i=='.' or i == "":
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        path = '/' + "/".join(stack)

        return path