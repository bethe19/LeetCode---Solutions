class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in paths:
            part = i.split(" ")
            root = part[0]
            for j in part[1:]:
                k = j.index('(')
                name = j[:k] 
                content = j[k:-1]
                map[content].append(root+'/'+name)
        result = []
        for key, value in map.items():
            if len(value) > 1:
                result.append(value)
        return result
